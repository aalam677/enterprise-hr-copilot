# Enterprise HR Copilot

A Multi-Agent Enterprise HR Copilot built using FastAPI, Streamlit, ChromaDB, OpenAI, Retrieval Augmented Generation (RAG), and Model Context Protocol (MCP).

The solution enables employees to interact with HR policies and enterprise HR tools through a conversational AI assistant.

## Features

- RAG-based HR Policy Assistant
- ChromaDB Vector Search
- Multi-Agent Architecture
- MCP Tools Integration
- Leave Balance Lookup
- Employee Search
- Holiday Calendar
- Leave Request Creation
- FastAPI Backend
- Streamlit UI

## Architecture

User -> Streamlit UI -> FastAPI -> Supervisor Agent -> Retrieval Agent / HR Tool Agent -> Response Agent

## Run

```bash
uvicorn mcp_server:app --reload --port 8001
uvicorn api:app --reload --port 8000
streamlit run streamlit_app.py
```

## Author

Alam MD
