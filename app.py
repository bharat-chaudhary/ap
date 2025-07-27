from flask import Flask, request, jsonify, render_template
from chat_service import ask_groq
from history_service import save_message, get_history
from knowledge_service import get_knowledge, search_knowledge
from search_service import search_history

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    if user_msg.lower().startswith("search:"):
        keyword = user_msg.split(":", 1)[1].strip()
        results = search_history(keyword)
        return jsonify(reply="\n".join(results) or "No results found.")

    if user_msg.lower().startswith("info:"):
        topic = user_msg.split(":", 1)[1].strip()
        return jsonify(reply=get_knowledge(topic))

    try:
        bot_reply = ask_groq(user_msg)
        save_message(user_msg, bot_reply)
        return jsonify(reply=bot_reply)
    except Exception as e:
        return jsonify(reply=f"Error: {str(e)}")

@app.route('/history')
def history_page():
    history = get_history()
    return render_template('history.html', history=history)

@app.route('/knowledge')
def knowledge_page():
    knowledge = get_knowledge()
    return render_template('knowledge.html', knowledge=knowledge)

@app.route('/search', methods=['GET', 'POST'])
def search_knowledge_page():
    query = None
    results = []
    searched = False

    if request.method == 'POST':
        query = request.form['query']
        results = search_knowledge(query)
        searched = True

    return render_template('search.html', results=results, query=query, searched=searched)

@app.route("/api/history")
def api_history():
    history = get_history()
    return jsonify(history)

@app.route("/recent-history")
def recent():
    recent = get_history(limit=10)
    return jsonify([
        {
            "user": h.get("user_message", ""), 
            "bot": h.get("bot_reply", "")
        }
        for h in recent
    ])

if __name__ == "__main__":
    app.run(debug=True)
