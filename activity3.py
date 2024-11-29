import re
import random

# Data structures for travel recommendations and jokes
destinations = {
    "countries": ["Nepal", "India", "United States"],
    "mountains": ["Mount Everest", "Mount Kailash", "Mount Annapurna"],
    "cities": ["Kathmandu", "Delhi", "Washington DC"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def greet():
    print("Hello! I am an AI TravelBot that will assist you with your travels.")
    username = input("May I get your name?: ")
    print(f"Nice to meet you, {username}. How can I assist you today?")

def show_help():
    print("""
I can assist you with the following tasks:
- Provide travel recommendations
- Check flight status
- Offer packing tips
- Tell some amazing jokes
- Ask me a question
- Type 'exit' to leave
""")

def process_input(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    return user_input

def provide_recom():
    print("Sure! Are you interested in countries, mountains, or cities?")
    preference = input().lower()
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"I recommend visiting {suggestion}. It's a wonderful choice!")
    else:
        print("Sorry, I don't have recommendations for that preference.")

def check_flight_status():
    statuses = ["On time", "Delayed", "Cancelled"]
    print(f"Your flight status is: {random.choice(statuses)}")

def packing_tips():
    tips = [
        "Roll your clothes to save space.",
        "Use packing cubes for better organization.",
        "Carry a portable charger in your bag.",
        "Always keep copies of your travel documents.",
        "Pack versatile clothing that you can mix and match."
    ]
    print(f"Packing tip: {random.choice(tips)}")

def tell_joke():
    print(f"Here's a joke for you: {random.choice(jokes)}")

def main():
    greet()
    while True:
        user_input = input("\nYou: ")
        processed_input = process_input(user_input)

        if "recommend" in processed_input:
            provide_recom()
        elif "flight" in processed_input:
            check_flight_status()
        elif "packing" in processed_input:
            packing_tips()
        elif "joke" in processed_input:
            tell_joke()
        elif "help" in processed_input:
            show_help()
        elif "exit" in processed_input:
            print("Goodbye! Safe travels!")
            break
        else:
            print("I didn't understand that. Type 'help' to see what I can do.")

# Start the chatbot
if __name__ == "__main__":
    main()