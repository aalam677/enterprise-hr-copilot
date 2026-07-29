# 🏢 Enterprise HR Copilot

A Multi-Agent Enterprise HR Copilot built using **FastAPI**, **Streamlit**, **OpenAI**, **ChromaDB**, **Retrieval-Augmented Generation (RAG)**, and **Model Context Protocol (MCP)**.

The solution enables employees to interact with HR policies and enterprise HR systems through an intelligent conversational assistant.

---

# 🚀 Features

## 📚 RAG-Based HR Policy Assistant

- Upload HR Policy PDFs
- Generate embeddings using OpenAI Embeddings
- Store vectors in ChromaDB
- Retrieve relevant policy context
- Answer policy-related questions

### Example

```text
What is the maternity leave policy?
```

---

## 🔧 MCP Enterprise Tools

### Leave Balance

```text
How many casual leaves do I have?
```

Returns:

- Annual Leave
- Casual Leave
- Sick Leave

---

### Employee Search

```text
Find employee John Smith
```

Returns:

- Name
- Department
- Designation

---

### Holiday Calendar

```text
Show holiday calendar for 2025
```

Returns company holiday information.

---

### Leave Request Creation

```text
Apply casual leave from 12 Aug to 14 Aug
```

Returns:

```text
Request ID
Status
```

Stores request details in:

```text
leave_requests.json
```

---

# 🤖 Multi-Agent Architecture

## Supervisor Agent

Responsible for:

- Intent Classification
- Agent Selection
- Workflow Orchestration
- Response Aggregation

---

## Policy Retrieval Agent

Responsible for:

- Vector Search
- ChromaDB Queries
- Context Retrieval
- Source Identification

---

## HR Tool Agent

Responsible for:

- Leave Balance Retrieval
- Employee Search
- Holiday Calendar Access
- Leave Request Creation

Uses MCP Server for enterprise tool integration.

---

## Response Agent

Responsible for:

- Combining RAG Context
- Combining MCP Results
- Generating Final Responses

---

# 🏗 Architecture

<img width="667" height="573" alt="image" src="https://github.com/user-attachments/assets/f3f1c688-c123-4b2b-8064-b9bb24abcbe4" />
