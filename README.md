
---

```markdown
# 🤖 Content Generation Agent

A scalable FastAPI-based multi-agent AI backend built using LangChain and LLM pipelines.  
This project processes user queries through structured agent workflows and returns refined responses.

---

## 🚀 Features

- ⚡ Async FastAPI backend
- 🧠 Multi-agent pipeline architecture
- 🔍 Review & refinement agent
- 🌐 SERP API integration
- 🔐 Environment-based configuration
- 📦 uv for dependency management
- 📘 Auto-generated Swagger documentation

---

## 🏗 Architecture

User Query  
↓  
Primary Agent  
↓  
Review Agent  
↓  
Final Response  

The system is modular and designed for scalability.

---

## 🛠 Tech Stack

- Python 3.11+
- FastAPI
- LangChain
- Pydantic
- Uvicorn
- uv (dependency manager)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/harsharora05/content-generation-agent.git
cd content-generation-agent
```

### 2️⃣ Install dependencies (using uv)

```bash
uv sync
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_key
SERPAPI_KEY=your_serpapi_key
```

⚠️ Do NOT commit your `.env` file.  
Use a `.env.example` file for sharing environment structure.

---

## ▶️ Run the Application

```bash
uv run main.py
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/generate`

### Request Body

```json
{
  "query": "What is 2 + 2?"
}
```

### Response

```json
{
  "success": true,
  "response": "4"
}
```
