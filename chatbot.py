def chatbot():
    print("Welcome to CodSoft Chatbot!")
    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("Bot: Hello! How can I help you?")
        elif 'your name' in user_input:
            print("Bot: I am CodSoft Bot.")
        elif 'phone number' in user_input or 'mobile' in user_input:
            print("Bot: You can contact us at +91-9876543210.")
        elif 'email' in user_input or 'mail' in user_input:
            print("Bot: You can email us at codsoft@example.com.")
        elif 'bye' in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
