from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from wellness import get_wellness_recommendations
from safety_filter import check_safety

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "response": "Please enter a message."
        })

    # Check message safety
    safety_result = check_safety(user_message)

    # Handle crisis or offensive messages
    if safety_result["type"] != "safe":
        return jsonify({
            "response": safety_result["message"]
        })

    # Generate AI response
    ai_response = get_response(user_message)

    # Get wellness recommendations
    wellness = get_wellness_recommendations(user_message)

    return jsonify({
        "response": ai_response,
        "wellness": wellness
    })


if __name__ == "__main__":
    app.run(debug=True)