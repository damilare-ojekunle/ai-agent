from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

llm = ChatOllama(model="qwen3:14b",temperature=0)

class AgentOutput(BaseModel):
    question:str = Field(description="Thee orginal question")
    reasoning:str = Field(description="Step by step thinking")
    result:str = Field(description="Final concise answer")

structured_llm = llm.with_structured_output(AgentOutput)
prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. Always reason step by step"),
    ("user","{question}")
])

chain = prompt | structured_llm
output = chain.invoke({
    "question":"What is the capital of Nigeria?"
})

print("Question:",output.question)
print("Reasoning:",output.reasoning)
print("Result",output.result)