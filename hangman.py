import random

# List of predefined words
words = ["apple", "tiger", "house", "robot", "green"]
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player guessed the word
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check the guess
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong Guess!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong_guesses:
    print("\nYou Lost!")
    print("The correct word was:", word)