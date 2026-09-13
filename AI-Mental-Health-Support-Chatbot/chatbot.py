from transformers import pipeline

# Load the conversational model
chatbot = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-small"
)

def get_response(user_message):
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