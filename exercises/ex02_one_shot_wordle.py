"""EX02 - One shot Wordle."""
__author__ = "730711512"

secret_word_guess: str = input("What is your 6-letter guess? ")
secret_word: str = "python"
emoji_string: str = ""

while len(secret_word_guess) != 6:
    secret_word_guess = input("That was not 6 letters! Try again ")
    
secret_word_guess_idx = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character_exists = False
alternate_idx = 0

while secret_word_guess_idx < len(secret_word):
    if secret_word_guess[secret_word_guess_idx] == secret_word[secret_word_guess_idx]:
        emoji_string += GREEN_BOX
    else: 
        character_exists = False
        alternate_idx = 0
        while not character_exists and alternate_idx < len(secret_word):
            if secret_word[alternate_idx] == secret_word_guess[secret_word_guess_idx]:
                character_exists = True
            else:
                alternate_idx = alternate_idx + 1 
    
        if character_exists:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX

    secret_word_guess_idx = secret_word_guess_idx + 1
print(emoji_string)

if secret_word == secret_word_guess:
    print("Woo! You got it! ")
else: 
    print("Not quite. Play again soon! ")