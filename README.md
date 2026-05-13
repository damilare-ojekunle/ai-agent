# Local AI Chat API

A production-ready AI API built with FastAPI and LangChain,
powered by Qwen 3 14B running locally via Ollama.

## What it does

- Accepts any question via REST API
- Returns structured JSON with reasoning and result
- Runs 100% locally - no API costs, no data leaving your machine

## Tech Stack

- Python
- FastAPI
- LangChain
- Ollama + Qwen 3 14B
- Pydantic

## How to run

1. Make sure Ollama is running with Qwen 3
2. Install dependencies: pip install -r requirements.txt
3. Start the API: uvicorn chat_api:app --reload
4. Send a POST request to http://localhost:8000/chat

## Example Request

{
"question": "What is Python?",
"topic": "programming"
}

## Example Response

{
"question": "What is Python?",
"reasoning": "...",
"result": "...",
"code_example": "..."
}

## Built by

Damilare Ojekunle - AI Engineer in training
