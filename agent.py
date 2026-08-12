#create simple ai agent using loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Process user input (simple rule-based response)
    if "hello" in user_input.lower():
        response = "Hello! How can I help you?"
    elif "how are you" in user_input.lower():
        response = "I'm doing well, thank you for asking!"
    elif "what is your name" in user_input.lower():
        response = "I am a simple AI agent."
    else:
        response = "I'm sorry, I don't understand that."

    # Display response
    print("AI: ", response)