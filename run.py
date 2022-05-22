import random
from words import list_of_words

# Defining variables

character = ""
right_characters = []
wrong_characters = []
tries = 6
game = False
guessed = False
random_word = random.choice(list_of_words)

# Start function


def start():
    name = input("What is your name? ")
    print("Hello " + name + "!")
    print("Welcome to Hangman!")
    print("Can you guess the secret word?")
    print("You have 6 tries, best of luck!")

