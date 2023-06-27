import random
import os

def run():
    IMAGE = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        "JAVA",
        "PHP",
        "PYTHON",
        "JAVASCRIPT"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attempts = 6
    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGE[attempts])
        letter = input("Choose a letter: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts -=1

        if "_" not in spaces:
            os.system("clear")
            print("You rock!")
            break

        if attempts == 0:
            os.system("clear")
            print("You suck!")
            break

        input()

if __name__ == "__main__":
    run()
