# AI-Mental-Health-Support-Chatbot
An AI chatbot that provides emotional support and personalized wellness recommendations using Python, Hugging Face Transformers, and Flask.
# AI Mental Health Support Chatbot

## Part 1: Project Setup

In this part, the basic project structure was created for the AI Mental Health Support Chatbot.

### Tools Used

* Python
* Flask
* Hugging Face Transformers
* PyTorch
* Pandas

### Project Setup

The required folders and files were created to organize the chatbot, wellness recommendation system, Flask application, frontend, and chat logs.

### Dependencies

The required Python libraries were added to `requirements.txt` and installed using:

```bash
pip install -r requirements.txt
```

This completes the basic project setup.
# Part 2: Wellness Recommendation System

In this part, a wellness recommendation system was added to the AI Mental Health Support Chatbot.

The system uses a CSV dataset to identify the user's situation and provide suitable wellness suggestions.

## Features

- Meditation recommendations
- Motivation and emotional support
- Mindful activities
- Healthy eating suggestions
- Sleep-related tips
- Singing and dancing activities
- Painting and creative activities
- Music suggestions
- Nature activities
- Trip and outing ideas
- Social connection
- Hobby suggestions

## Tools Used

- Python
- Pandas
- CSV Dataset

## How It Works

1. The user's message is converted to lowercase.
2. Keywords are used to identify the user's situation.
3. The matching situation is searched in the wellness CSV dataset.
4. Relevant wellness recommendations are returned.
5. If no matching situation is found, general wellness recommendations are provided.

## File Used

`wellness.py`

`wellness_recommendations.csv`

## Testing

The system was tested with the message:
# Part 3: Safety Filter

A basic safety filter was added to make the chatbot more responsible and supportive.

## Features

- Detects basic crisis-related keywords
- Handles offensive language
- Provides a clear disclaimer
- Reminds users that the chatbot is not a mental health professional
- Encourages users to contact trusted people, qualified professionals, or emergency services when appropriate

## Tools Used

- Python

## How It Works

1. The user's message is converted to lowercase.
2. The message is checked for crisis-related keywords.
3. Offensive words are also checked.
4. A suitable safety response is returned based on the message.
5. Normal messages receive a general emotional-support disclaimer.

## Testing

The safety filter was tested with:

"I am feeling stressed today"

The system successfully classified the message as safe and returned the appropriate disclaimer.

"I am feeling stressed today"

The system successfully returned recommendations for meditation, motivation, mindful activities, healthy eating, sleeping, singing, dancing, painting, music, nature, trips, social connection, and hobbies.
# Part 4: Flask Backend

In this part, a Flask backend was created for the AI Mental Health Support Chatbot.

## Features

- Flask web application
- Home route for the chatbot interface
- `/chat` API endpoint for user messages
- Connects AI chatbot with the Flask backend
- Connects wellness recommendation system
- Connects safety filter
- Returns chatbot and wellness responses in JSON format

## Tools Used

- Python
- Flask
- Hugging Face Transformers
- Pandas

## How It Works

1. User sends a message through the web interface.
2. Flask receives the message.
3. The safety filter checks the message.
4. The AI chatbot generates a response.
5. The wellness system provides relevant suggestions.
6. Flask sends the response back to the frontend.

## Testing

The Flask application was successfully started using:

```bash
python app.py
