from fastapi import FastAPI
from pydantic import BaseModel,Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

app = FastAPI()
llm = ChatOllama(model="qwen3:14b",temperature=0)
class QuestionInput(BaseModel):
    question:str
    topic:str ="general knowledge"

class AnswerOutput(BaseModel):
    question:str = Field(description="The orginal question")
    reasoning:str =Field(description="Step by step thinking")
    result:str = Field(description="Final concise answer")
    code_example: str = ""



# prompt = ChatPromptTemplate([
#     ("system","You an expert in {topic}.Reason step by step"),
#     ("user","{question}")
# ])

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert in {topic}.
Always respond with valid JSON only. No extra text.
Format:
{{
  "question": "the original question",
  "reasoning": "your step by step thinking",
  "result": "your final concise answer",
  "code_example": "any code example here, or empty string if no code needed"
}}"""),
    ("user", "{question}")
])

chain = prompt | llm | StrOutputParser()

@app.post("/chat")

def chat(input:QuestionInput):
    response = chain.invoke(
        {
            "topic":input.topic,
            "question":input.question
        }
    )
    data = json.loads(response)
    return AnswerOutput(**data)
@app.get('/')
def root():
    return {"status":"API Agent is Running"}
