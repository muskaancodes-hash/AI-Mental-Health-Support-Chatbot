from transformers import pipeline

# Load the conversational model
chatbot = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-small"
)

def get_response(user_message):
    emotional = emotional_response(user_message)

    if emotional:
        return emotional
    prompt = f"User: {user_message}\nBot:"

    result = chatbot(
        prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7
    )

    response = result[0]["generated_text"]

    # Get only the bot's response
    if "Bot:" in response:
        response = response.split("Bot:")[-1].strip()

    return response
# Emotional support responses

def emotional_response(user_message):
    message = user_message.lower().strip()

    if any(word in message for word in ["stressed", "stress", "pressure"]):
        return "Hey, that sounds really stressful. ❤️ You don't have to handle everything at once. Take a slow breath and tell me what's been bothering you. I'm here to listen."

    if any(word in message for word in ["sad", "upset", "crying", "unhappy"]):
        return "I'm sorry you're having a difficult moment. 💜 It's okay to feel sad. If you want, you can tell me what's on your mind. I'm here to listen."

    if any(word in message for word in ["lonely", "alone"]):
        return "Feeling lonely can be really hard. 🤍 I'm glad you reached out. You don't have to keep everything to yourself. Want to tell me what's making you feel alone?"

    if any(word in message for word in ["angry", "mad", "frustrated"]):
        return "It sounds like you're really frustrated right now. 💜 Take a moment and breathe. You can tell me what happened — I'm listening."

    if any(word in message for word in ["tired", "exhausted"]):
        return "You sound really tired. 🫂 Maybe you need a little break instead of pushing yourself harder. Be gentle with yourself today."

    if any(word in message for word in ["anxious", "anxiety", "worried", "nervous"]):
        return "I can understand why that might feel overwhelming. 💜 Take one slow breath with me. You don't have to figure everything out right now. Tell me what you're worried about."

    return None