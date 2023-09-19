"""EX02 - One shot Wordle"""
__author__ = "730711512"

secret_word_guess: str = input("What is your 6-letter guess? ")
secret_word: str = "python"

secret_word: len = 6

while len(secret_word_guess) == secret_word:
    print("Not quite. Play again soon! ")
if len(secret_word_guess) != secret_word:
    print("That was not 6 letters! Try again ")
if secret_word_guess == secret_word:
    print("Woo! You got it!")

secret_word_guess_idx: int = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while secret_word[0] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[0] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1

while secret_word[1] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[1] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1

while secret_word[2] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[2] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1

while secret_word[3] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[3] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1

while secret_word[4] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[4] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1

while secret_word[5] == secret_word_guess:
    print("\U0001F7E9")
    if secret_word[5] != secret_word_guess:
        print("\U00002B1C")
        secret_word_guess_idx = secret_word_guess_idx + 1