
import random

words = ["apple", "python", " mango", "school", "coding"]

word = random.choice(words).strip()
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    if display_word == word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess!")

if incorrect_guesses == max_guesses:
    print("\nGame over! The word was:", word)
