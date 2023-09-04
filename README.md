# Hangman Game

**Created by:** Swadheen Mishra, Class 10, for a Byte Club Project

## Introduction

I'm Swadheen Mishra, a class 10 student, and I've created this Hangman game as part of a Byte Club project. It's a Python program that lets you play the classic word-guessing game in the command line. See if you can guess the hidden word with limited incorrect attempts! Have fun playing!

## Game Rules

- You have a maximum of 6 incorrect guesses before you lose the game.
- You can only guess one letter at a time.
- If you guess a letter that is in the word, it will be revealed in its correct position(s).
- If you guess a letter that is not in the word, it will be added to your list of incorrect guesses.
- You win the game if you correctly guess all the letters in the word before running out of attempts.
- The game will provide hints in the form of blank spaces representing the letters in the word.

## How to Run

1. Make sure you have Python installed on your computer.

2. Clone the repository or download the Python script to your local machine.

3. Install the required dependency 'termcolor' using pip:

4. Open your terminal or command prompt and navigate to the directory where the script is located.

5. Run the script using the following command:

6. Follow the on-screen instructions to play the game.

## Code Structure

- `man` class: Defines the hangman figure's appearance and contains methods for checking if the game is still in progress and displaying the hangman.

- `find_in_string` function: Finds all occurrences of a letter in a string.

- `make_hintBox` function: Creates a list of underscores representing the hidden word.

- `get_random_words` function: Retrieves a random word from an online API.

- `Start_game` function: The main game loop that handles game logic and user input.

- `main` function: The entry point of the program, allowing you to start the game and choose the word's length.

Enjoy playing Hangman! Good luck!
