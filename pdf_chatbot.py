from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print("Loading PDF ...")
loader = PyPDFLoader("LABOUR_ACT.pdf")
pages = loader.load()
print(f"Loaded {len(pages)} pages")

print("Splitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap= 50
)
chunks = splitter.split_documents(pages)
print(f"Created {len(chunks)} chunks")
print("Creating vector store...")
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
print("Vector store ready")

retriver = vectorstore.as_retriever(
    search_kwargs={"k":5}
)

prompt = ChatPromptTemplate.from_messages([
    ("system",""" You are a Nigerian Labour Law Expert.
Answer questions using ONLY context provided below.
If the answer is not in the context,say "I could not find that in the Labour Act."

Context:
     {context} """),
("user","{question}")
])

llm = ChatOllama(model="qwen3:14b",temperature=0)
chain = prompt | llm | StrOutputParser()

def ask(question):
    print(f"\nQuestion:{question}")
    docs = retriver.invoke(question)
    context ="\n\n".join([doc.page_content for doc in docs])
    answer = chain.invoke({
        "context":context,
        "question":question
    })
    print(f"Answer:{answer}")
ask("What does the Labour Act say about hours of work and overtime?") 