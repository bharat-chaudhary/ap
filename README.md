# 🤖 AI Chat Microservices App

A modular Flask-based chatbot web application using microservices architecture, integrating OpenAI (Groq), MongoDB, and a knowledge base.

---

## 🧩 Project Architecture

This system is divided into the following microservices:

| Service              | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `chat_service.py`    | Handles message forwarding to Groq API (OpenAI-compatible) and returns response. |
| `history_service.py` | Stores and retrieves chat messages from MongoDB.              |
| `knowledge_service.py` | Loads static knowledge base from JSON and provides retrieval/search. |
| `search_service.py`  | Searches previous history entries for keyword matches.        |
| `app.py`             | Main Flask app that coordinates the above services and serves web routes. |

---

## 🗂 File Structure

```
.
├── app.py                   # Flask application
├── chat_service.py          # Handles AI responses
├── history_service.py       # MongoDB storage and retrieval
├── knowledge_service.py     # Static knowledge loading & querying
├── search_service.py        # Search over chat history
├── templates/
│   ├── index.html           # Main chat UI
│   ├── history.html         # Full chat history with delete feature
│   ├── knowledge.html       # View static knowledge base
│   └── search.html          # Search knowledge base
├── static/
│   └── (optional CSS/JS)    # Styling or JS files if separated
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🛢 Database Setup

This project uses MongoDB to store chat history.

- **Default connection:** `mongodb://localhost:27017/`
- **Database name:** `chatdb`
- **Collection name:** `history`

Ensure MongoDB is running locally. You can install MongoDB or use MongoDB Atlas (update the URI in `history_service.py`).

---

## ⚙ Setup Instructions

1. **Clone this repo:**
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

---

## 🔗 API Endpoints

| Endpoint               | Method     | Description                                  |
|------------------------|------------|----------------------------------------------|
| `/`                    | GET        | Main chat page                               |
| `/chat`                | POST       | Accepts user message, returns AI response    |
| `/history`             | GET        | View chat history (HTML view)                |
| `/api/history`         | GET        | API to get chat history in JSON              |
| `/delete-history/<id>` | DELETE     | Deletes a single message from DB             |
| `/knowledge`           | GET        | View all knowledge base items                |
| `/search`              | GET/POST   | Search knowledge base                        |
| `/recent-history`      | GET        | Fetch recent 10 messages                     |

---

## 🧠 Knowledge Base

Stored as a JSON file loaded by `knowledge_service.py`

**Example format:**
```json
[
  {
    "topic": "Python",
    "answer": "Python is a popular programming language for web, AI, and more."
  }
]
```

---

## ✅ Features

- Microservices architecture for modular code
- MongoDB chat history with deletion support
- Groq API (OpenAI-compatible) for responses
- Knowledge base support
- Keyword search over history and knowledge
- Mobile-friendly and dark-mode UI

---

## 🚀 Deployment

To deploy on services like Render, Railway, or Heroku:

- Add environment variable for MongoDB URI if using cloud DB
- Use `gunicorn` + `Procfile` for production

---

## 📄 License

This project is open-source and free to use for educational purposes.
