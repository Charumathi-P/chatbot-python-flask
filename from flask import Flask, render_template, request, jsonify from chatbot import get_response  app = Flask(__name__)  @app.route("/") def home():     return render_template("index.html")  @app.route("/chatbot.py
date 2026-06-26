import random

responses = {
    "hello": [
        "Hello! 👋",
        "Hi there!",
        "Hey! How can I help you?"
    ],

    "hi": [
        "Hello!",
        "Hi! 😊",
        "Welcome!"
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine. Thanks for asking.",
        "I'm always ready to help."
    ],

    "what is your name": [
        "I'm FlaskBot.",
        "My name is Flask ChatBot.",
        "You can call me FlaskBot."
    ],

    "bye": [
        "Goodbye!",
        "See you soon!",
        "Have a wonderful day!"
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime 😊"
    ]
}

def get_response(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return random.choice(responses[key])

    return "Sorry, I don't understand. Can you ask something else?"
