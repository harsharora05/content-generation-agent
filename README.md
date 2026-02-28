
# 📄 README.md

````markdown
# 🤖 Content Agent – Multi-Agent AI Backend

A scalable FastAPI-based multi-agent system built using LangChain and LLM pipelines.  
This project processes user queries through structured agent workflows and returns refined responses.

---

## 🚀 Features

- ⚡ FastAPI async backend
- 🧠 Multi-agent pipeline architecture
- 🔍 Review & refinement agent
- 🌐 SERP API integration (if enabled)
- 🔐 Environment-based configuration
- 📦 uv for dependency management
- 📘 Auto-generated Swagger docs

---

## 🏗 Architecture

User Query  
↓  
Primary Agent  
↓  
Review Agent (Refactor & Validate Output)  
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
git clone https://github.com/your-username/your-repo.git
cd your-repo
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

⚠️ Do NOT commit `.env`
Use `.env.example` for reference.

---

## ▶️ Run the Application

```bash
uv run main.py
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/generate`

#### Request Body

```json
{
  "query": "What is 2 + 2?"
}
```

#### Response

```json
{
  "success": true,
  "response": "4"
}
```

---

