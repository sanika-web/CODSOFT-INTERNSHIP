def chatbot():
    print("🤖 Hello! I’m your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello! How can I help you today?")
        elif 'how are you' in user_input:
            print("Bot:I'm doing fine. How about you?")
        elif 'name' in user_input:
            print("Bot: I'm a smart AI rule-based chatbot!")
        elif 'bye' in user_input:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm not sure how to respond to that. Try asking something else.")
chatbot()


