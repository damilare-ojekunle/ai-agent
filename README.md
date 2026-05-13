---

# Nigerian Labour Act PDF Chatbot

A production-ready AI chatbot that allows users to query the Nigerian
Labour Act using natural language. Instead of manually searching through
82 pages of legal text, users can ask plain English questions and receive
precise, document-grounded answers. The system only answers from the
actual document — it does not hallucinate or rely on general training
knowledge.

## How it works

The system is built using a RAG (Retrieval Augmented Generation) pipeline.
The Labour Act PDF is loaded, split into 486 chunks, and converted into
vector embeddings using nomic-embed-text. These embeddings are stored in
ChromaDB for fast similarity search. When a user asks a question, the most
relevant chunks are retrieved and injected into the prompt context. Qwen 3
14B running locally via Ollama then generates a precise answer grounded in
the document — with zero API costs and complete data privacy.

## Tech Stack

- Python
- LangChain
- ChromaDB
- nomic-embed-text (embeddings)
- Ollama + Qwen 3 14B (generation)
- PyPDF

## How to run

1. Make sure Ollama is running with Qwen 3 and nomic-embed-text
2. Install dependencies: pip install -r requirements.txt
3. Place your PDF in the project folder
4. Run: python3 pdf_chatbot.py

## Example Questions

- "What are the working hours for young persons?"
- "What does the Labour Act say about overtime?"
- "What are the rights of an employee upon termination?"

## Built by

Damilare Ojekunle - AI Engineer in training
