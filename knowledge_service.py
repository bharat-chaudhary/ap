knowledge_base = {
    "groceries": "Groceries include fruits, vegetables, dairy products, and other essentials.",
    "storage": "Store perishable items in the fridge. Dry goods in a cool, dark place.",
    "agriculture": "Agriculture involves cultivating soil, growing crops, and raising animals.",
    "organic farming": "Organic farming uses natural fertilizers and pest control without synthetic chemicals.",
    "agri-tech": "Agri-tech refers to the use of technology to improve farming efficiency and yield."
    # Add more as needed
}

def get_knowledge(topic=None):
    if not topic:
        return knowledge_base
    return knowledge_base.get(topic.lower(), "No information available on that topic.")

def search_knowledge(query):
    return [f"{k}: {v}" for k, v in knowledge_base.items() if query.lower() in k.lower()]
