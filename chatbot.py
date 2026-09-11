def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined keyword-based responses
    responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! Great to talk to you.",
        "how are you": "I'm just a Python script, but I'm functioning perfectly! How are you?",
        "what is your name": "I am CodeAlpha Bot, your assistant.",
        "who created you": "I was built by a developer during the CodeAlpha Internship Program!",
        "python": "Python is an amazing programming language for AI, web dev, and automation!",
        "bye": "Goodbye! Have a fantastic day ahead!",
        "exit": "Goodbye! Have a fantastic day ahead!"
    }

    # Match user input with predefined responses
    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm sorry, I didn't quite understand that. Try asking something else!"

def main():
    print("========================================")
    print("       CodeAlpha Basic Chatbot          ")
    print("========================================")
    print("Start chatting! Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_msg = input("You: ")
        
        if not user_msg.strip():
            continue

        bot_msg = get_bot_response(user_msg)
        print(f"Bot: {bot_msg}\n")

        if user_msg.lower().strip() in ["bye", "exit"]:
            break

if __name__ == "__main__":
    main()
