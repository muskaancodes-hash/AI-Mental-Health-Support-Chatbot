import pandas as pd

# Load wellness dataset
df = pd.read_csv("wellness_recommendations.csv")


def get_wellness_recommendations(user_message):
    user_message = user_message.lower()

    # Keywords for different situations
    situation_keywords = {
        "stress": ["stress", "stressed", "pressure", "tension"],
        "anxiety": ["anxiety", "anxious", "worried", "worry", "nervous"],
        "sadness": ["sad", "unhappy", "crying", "upset"],
        "loneliness": ["lonely", "alone", "isolated"],
        "anger": ["angry", "anger", "mad", "furious"],
        "overthinking": ["overthinking", "overthink", "thinking too much"],
        "sleep_issue": ["sleep", "sleeping", "insomnia", "can't sleep"],
        "study_stress": ["study", "studying", "exam", "assignment"],
        "low_motivation": ["motivation", "motivated", "lazy", "unmotivated"],
        "low_mood": ["low mood", "feeling low", "down"],
        "frustration": ["frustrated", "frustration"],
        "boredom": ["bored", "boring", "boredom"],
        "social_stress": ["social", "friends", "people"],
        "work_pressure": ["work", "job", "workload"],
        "exam_stress": ["exam", "exams", "test"],
        "grief": ["loss", "grief", "lost someone"],
        "confidence_low": ["confidence", "insecure", "not good enough"]
    }

    situation = "general_wellness"

    for key, keywords in situation_keywords.items():
        if any(word in user_message for word in keywords):
            situation = key
            break

    # Find recommendations
    result = df[df["situation"] == situation]

    if result.empty:
        result = df[df["situation"] == "general_wellness"]

    recommendations = result.iloc[0]

    return {
        "meditation": recommendations["meditation"],
        "motivation": recommendations["motivation"],
        "mindful_activity": recommendations["mindful_activity"],
        "healthy_eating": recommendations["healthy_eating"],
        "sleeping": recommendations["sleeping"],
        "singing": recommendations["singing"],
        "dancing": recommendations["dancing"],
        "painting": recommendations["painting"],
        "music": recommendations["music"],
        "nature_activity": recommendations["nature_activity"],
        "trip_idea": recommendations["trip_idea"],
        "social_connection": recommendations["social_connection"],
        "hobby": recommendations["hobby"]
    }