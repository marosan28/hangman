import random
import pyfiglet
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
    heading = pyfiglet.figlet_format("HANGMAN")
    print(heading)
    name = input("What is your name? ")
    print("Hello " + name + "!")
    print("Welcome to Hangman!")
    print("Can you guess the secret word?")
    print("You have 6 tries, best of luck!")


def pick_word():
    return random_word.lower()


def guessed_word():
    global right_characters
    for x in range(0, len(random_word)):
        character = random_word[x]
        if character in right_characters:
            print(character, end=" ")
        else:
            print("_", end=" ")
    print("")


def main():
    start()


if __name__ == '__main__':
    main()
