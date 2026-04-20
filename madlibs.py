import random

def zoo_story():
    """Zoo adventure madlibs"""
    print("\n🦁 ZOO ADVENTURE 🦁")
    adjective1 = input("Enter an adjective (description): ")
    noun1 = input("Enter a noun (person, place, or thing): ")
    adjective2 = input("Enter another adjective: ")
    verb1 = input("Enter a verb ending in 'ing': ")
    adjective3 = input("Enter another adjective: ")
    
    print("\n" + "="*50)
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit, I saw a {noun1}.")
    print(f"The {noun1} was {adjective2} and {verb1}.")
    print(f"I was {adjective3}!")
    print("="*50 + "\n")

def vacation_story():
    """Vacation madlibs"""
    print("\n✈️  VACATION STORY ✈️")
    destination = input("Enter a destination (place): ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adjective2 = input("Enter another adjective: ")
    plural_noun = input("Enter a plural noun: ")
    number = input("Enter a number: ")
    
    print("\n" + "="*50)
    print(f"I went to {destination} for vacation.")
    print(f"It was {adjective1} and full of {plural_noun}.")
    print(f"I found a {noun1} and {verb1} it.")
    print(f"That was the most {adjective2} moment ever!")
    print(f"I spent ${number} and had the time of my life.")
    print("="*50 + "\n")

def restaurant_story():
    """Restaurant madlibs"""
    print("\n🍕 RESTAURANT DISASTER 🍕")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adjective2 = input("Enter another adjective: ")
    food = input("Enter a type of food: ")
    person = input("Enter a person's name: ")
    number = input("Enter a number: ")
    
    print("\n" + "="*50)
    print(f"I went to a {adjective1} restaurant last night.")
    print(f"I ordered a {noun1} with {food} on the side.")
    print(f"A waiter {verb1} and spilled {food} on my shirt!")
    print(f"My friend {person} laughed so hard.")
    print(f"I got out of paying the ${number} bill and got free dessert!")
    print("="*50 + "\n")

def play_game():
    """Main game loop"""
    print("\n" + "🎮 "*15)
    print("WELCOME TO MADLIBS!")
    print("🎮 "*15 + "\n")
    
    while True:
        print("Choose a story:")
        print("1. Zoo Adventure")
        print("2. Vacation Story")
        print("3. Restaurant Disaster")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            zoo_story()
        elif choice == "2":
            vacation_story()
        elif choice == "3":
            restaurant_story()
        elif choice == "4":
            print("\nThanks for playing! 👋")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    play_game()