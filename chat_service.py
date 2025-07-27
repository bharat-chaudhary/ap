import os
import requests
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Or hardcode it temporarily for testing
GROQ_MODEL = "llama3-70b-8192"  # ← Replace old model name


def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if response.status_code == 200:
        return data['choices'][0]['message']['content'].strip()
    else:
        raise Exception(data.get("error", {}).get("message", "Unknown error"))
