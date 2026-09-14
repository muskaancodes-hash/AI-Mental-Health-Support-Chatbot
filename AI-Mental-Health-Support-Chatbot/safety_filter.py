# Basic safety filter for the chatbot

# Words/phrases that may indicate a crisis situation
crisis_keywords = [
    "kill myself",
    "suicide",
    "end my life",
    "want to die",
    "i want to die",
    "hurt myself",
    "self harm",
    "self-harm"
]

# Basic offensive words
offensive_words = [
    "stupid",
    "idiot",
    "shut up"
]


def check_safety(user_message):
    message = user_message.lower().strip()

    # Check for crisis-related messages
    for keyword in crisis_keywords:
        if keyword in message:
            return {
                "type": "crisis",
                "message": (
                    "I'm really sorry you're going through this. "
                    "I'm not a mental health professional; I'm here only "
                    "to provide general emotional support and wellness suggestions. "
                    "If you may be in immediate danger, please contact your local "
                    "emergency service or reach out to a trusted person right now. "
                    "For ongoing support, consider contacting a qualified mental "
                    "health professional."
                )
            }

    # Check for offensive language
    for word in offensive_words:
        if word in message.split():
            return {
                "type": "offensive",
                "message": (
                    "Let's keep the conversation respectful. "
                    "I'm here to provide supportive and helpful guidance."
                )
            }

    # Normal message
    return {
        "type": "safe",
        "message": (
            "I'm not a mental health professional. "
            "I'm here to provide general emotional support "
            "and wellness suggestions."
        )
    }