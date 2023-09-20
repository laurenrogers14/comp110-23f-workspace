"""EX02 - One shot Wordle"""
__author__ = "730711512"

secret_word_guess: str = input("What is your 6-letter guess? ")
secret_word: str = "python"

while len(secret_word_guess) != 6:
    print("That was not 6 letters! Try again ")
    if secret_word_guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon! ")

secret_word_guess_idx = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character_exists = False
alternate_idx = 0

while secret_word[0] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[0] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1 
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

while secret_word[1] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[1] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

while secret_word[2] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[2] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

while secret_word[3] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[3] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

while secret_word[4] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[4] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

while secret_word[5] == secret_word_guess:
    print("\U0001F7E9")
    secret_word_guess_idx = secret_word_guess_idx + 1
    if secret_word[5] != secret_word_guess:
        print("\U00002B1C")
while not character_exists and alternate_idx < len(secret_word):
    if secret_word == secret_word_guess_idx:
        character_exists = True
    else:
        alternate_idx = alternate_idx + 1
    if character_exists:
        print("\U0001F7E8")
    else: 
        print ("\U00002B1C")

