from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(
    model="qwen3:14b",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {topic}. Explain simply."),
    ("user", "{question}")
])

chain = prompt | llm | StrOutputParser()

for chunk in  chain.stream({
   "topic": "AI Enginner",
    "question": "Fundamental knowledge needed to be a top 1% in AI enginnering "
}):
    print(chunk,end="",flush=True)

# messages = [
#     SystemMessage(content="You are a Python teacher who explains everything like the student is 10 years old. "),
#     HumanMessage(content="What is LangChain in one sentence")
# ]

# response = llm.invoke(messages)
# print(response.content)
