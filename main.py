
import random

name = input("What's your name? ")  # User will enter their name
print("Enjoy, " + name + "!")
words = ['python', 'coding', 'keyboard', 'methods', 'clouds', 'chicken', 'tree', 'water', 'table', 'lamp', 'towel', 'favorite']
word = random.choice(words)

print("Guess the word!")
guesses = ''
turns = 9

while turns > 0:
    failed = 0

    for letter in word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou win!")
        print("The word is:", word)
        break  # Exit the loop if the player wins

    print()

    guess = input("Choose a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

    print("The number of turns you have left is:", turns)

    if turns == 0:
        print("You lost. Better luck next time!")
        print("The word was:", word)
