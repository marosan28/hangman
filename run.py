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
    print("Please press ENTER after every entry")


def pick_word():
    return random_word.lower()


'''
Function printing guessed letters/underscores with the length of the word
'''


def guessed_word():
    global right_characters
    for x in range(0, len(random_word)):
        character = random_word[x]
        if character in right_characters:
            print(character, end=" ")
        else:
            print("_", end=" ")
    print("")


def one_character():
    global character
    right_character = False

    while right_character is False and tries > 0:
        character = input("Please enter a letter: ").lower()
        if character in right_characters or character in wrong_characters:
            print("You have already guessed the letter " + character)
        elif character.isalpha():
            if len(character) > 1 or len(character) <= 0:
                print("Letter can only be 1 character long!")
            else:
                right_character = True
        else:
            print("Oops! That's not a valid letter. Try again!")
    return character

# Function appends letters to wrong, changing number of tries.


def guess_character():
    global tries
    character = one_character()
    if character in random_word:
        right_characters.append(character)
    else:
        wrong_characters.append(character)
        tries -= 1


def main():
    start()
    guessed_word()
    one_character()
    guess_character()


if __name__ == '__main__':
    main()
