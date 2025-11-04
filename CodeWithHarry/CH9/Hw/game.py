import random
def game():
    print("Welcome to the game!")
    print("Instructions:")
    print("1. Choose a character.")
    print("2. Explore the world.")
    print("3. Complete quests.")
    print("Good luck!")
    print("Game started!")
    print("Explore your surroundings.")
    print("Interact with characters.")
    print("Complete your quests.")
    print(random.randint(1, 100))
    if random.randint(1, 100) > 50:
        print("You found a treasure!")
    else:
        print("You encountered a monster!")
    print("Game over!")

game()