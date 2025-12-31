print("Hello! I am a simple chatbot 🤖")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. What about you?")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
