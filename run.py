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


'''
Displays hangman depending on tries left. 
CREDIT for hangman display: 
https://inventwithpython.com/invent4thed/chapter8.html
'''


def hangman():
    global tries

    if tries == 6:
        print("-------------")
        print(" |           |")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("---------")
    elif tries == 5:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" | ")
        print(" | ")
        print(" | ")
        print("---------")
    elif tries == 4:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" |           |")
        print(" | ")
        print(" | ")
        print("---------")
    elif tries == 3:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" |           |")
        print(" |          /")
        print(" | ")
        print("---------")
    elif tries == 2:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" |           |")
        print(" |          / \\")
        print(" | ")
        print("---------")
    elif tries == 1:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" |           |\\")
        print(" |          / \\")
        print(" | ")
        print("---------")
    elif tries == 0:
        print("-------------")
        print(" |           |")
        print(" |           O")
        print(" |          /|\\")
        print(" |          / \\")
        print(" | ")
        print("---------")


# Checks if User has correctly guessed the word or not.


def check_game():
    global game

    if tries <= 0:
        hangman()
        game = True
        print("The word was " + random_word + ". Try again!")
    else:
        correct_word = True
        for character in random_word:
            if character not in right_characters:
                correct_word = False
                break
        if correct_word:
            game = True
            print("You win!")
    while game is False:
        hangman()
        guessed_word()

        if len(wrong_characters) > 0:
            print("guessed letters: ", wrong_characters)
        guess_character()
        check_game()


def main():
    global random_word
    start()
    pick_word()
    hangman()
    guess_character()
    guessed_word()
    check_game()


if __name__ == '__main__':
    main()
