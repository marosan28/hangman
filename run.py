import random
import pyfiglet
from words import list_of_words
from time import sleep

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
    sleep(1.2)
    print("Welcome to Hangman!")
    sleep(1.2)
    print("Can you guess the secret word?")
    sleep(1.2)
    print("You have 6 tries, best of luck!")
    sleep(1.6)
    print("=================================================================")
    sleep(2)
    print("Please press ENTER to start")


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
