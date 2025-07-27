from history_service import collection

def search_history(keyword):
    results = collection.find({
        "$or": [
            {"user_message": {"$regex": keyword, "$options": "i"}},
            {"bot_reply": {"$regex": keyword, "$options": "i"}}
        ]
    }).sort("timestamp", -1)

    return [f"You: {r['user_message']}\nBot: {r['bot_reply']}" for r in results]
