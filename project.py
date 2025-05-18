from textblob import TextBlob

# Define intents with keywords and responses
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9 AM to 9 PM Monday to Friday."
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I am sorry to hear that. I will connect you with our customer service team."
    },
}

def get_response(message):
    """Generate a response based on user message."""
    message = message.lower()

    # Check for matching intent keywords
    for intent_data in intents.values():
        if any(keyword in message for keyword in intent_data["keywords"]):
            return intent_data["response"]

    # Analyze sentiment if no intent matches
    sentiment = TextBlob(message).sentiment.polarity

    if sentiment > 0:
        return "I'm glad to hear that! How else can I assist you?"
    elif sentiment < 0:
        return "I'm sorry to hear that. Is there anything I can do to help?"
    else:
        return "I didn't quite catch that. Could you please elaborate?"

def chat():
    """Start the chatbot interaction."""
    print("Chatbot: Hi there! I'm here to help. What can I do for you today? (Type 'exit', 'quit', or 'bye' to end the chat)")
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Take care! If you need anything else, feel free to reach out. Goodbye!")
            break
        print(f"\nChatbot: {get_response(user_message)}\n")

if __name__ == "__main__":
    chat()
