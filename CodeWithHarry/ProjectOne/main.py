import random

# Dictionary for choices
youDict = {"s": 1, "w": -1, "g": 0}

# Computer choice (random from -1, 0, 1)
computer = random.choice([-1, 0, 1])

# User input with validation
while True:
    you = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    if you in youDict:
        youNum = youDict[you]
        break
    else:
        print("Invalid choice! Please enter 's', 'w', or 'g'.")

print(f"Computer chose: {computer}, You chose: {youNum}")

# Game logic
if computer == youNum:
    print("It's a tie!")
elif (computer == 1 and youNum == -1) or (computer == -1 and youNum == 0) or (computer == 0 and youNum == 1):
    print("Computer wins!")
else:
    print("You win!")

# Keep the console window open
input("\nPress Enter to exit...")