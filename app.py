from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("AIzaSyCFw9rBV3iYFGbS897hJyCLlP0iLuGS_iM"))

SYSTEM_PROMPT = """
You are my personal AI assistant.
Explain everything in simple Hinglish.
Follow my rules only.
"""

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    chat_history.append(f"You: {user_message}")

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=[
            SYSTEM_PROMPT,
            *chat_history
        ]
    )

    ai_reply = response.text
    chat_history.append(f"AI: {ai_reply}")

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)