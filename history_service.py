from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.chatdb
collection = db.history

def save_message(user_msg, bot_reply):
    collection.insert_one({
        "user_message": user_msg,
        "bot_reply": bot_reply,
        "timestamp": datetime.utcnow()
    })

def get_history(limit=50):
    return list(collection.find().sort("timestamp", -1).limit(limit))
