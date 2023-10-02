"""EX03 - Structured Wordle."""

__author__ = "730711512"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(any_length: str, single_character: str) -> bool:
    """Returns True if the single character is found at any index of the first string."""
    assert len(single_character) == 1
    if single_character in any_length:
        return True
    else:
        return False

def emojified(string_guess: str, string_secret: str) -> str:
    """This function checks for correct emoji matches indices."""
    assert len(string_guess) == len(string_secret)
    emoji: str = ""
    string_guess_idx = 0
    total: int = len(string_guess) - 1
    while string_guess_idx <= total:
        if contains_char(string_guess, string_secret[string_guess_idx]) is True and string_guess[string_guess_idx] != string_secret:
            emoji += YELLOW_BOX
        if contains_char(string_guess, string_secret[string_guess_idx]) is True and string_guess[string_guess_idx] == string_secret:
            emoji += GREEN_BOX
        if contains_char(string_guess, string_secret[string_guess_idx]) is False:
            emoji += WHITE_BOX
        string_guess_idx += 1
    return (emoji)

        
def input_guess(expected_length: int) -> str:
    secret_word_guess: str = input(f"Enter a {expected_length} character letter word")
    while secret_word_guess != expected_length:
        if len(secret_word_guess) > len(expected_length) or len(secret_word_guess) < len(expected_length):
            secret_word_guess = input(f"That wasn't {expected_length} chars! Try again")
    return secret_word_guess

string_secret: str = "codes"
def main() -> None:
    """The extry point of the program and main game loop."""
    # Your code will go here
    string_guess: str = ""
    string_secret: str = "codes"
    count = 1
    while string_guess != string_secret:
        print(f"===Turn {count}/6===")
        string_guess == input_guess(len(string_secret))
        print(emojified(string_guess, string_secret))
        if count <= 6 and string_guess != string_secret:
            count += 1
        if count <= 6 and string_guess == string_secret:
            print(f"You won in {count}/6 turns! ")
        if count == 7:
            print("X/6 -- Sorry, try again tomorrow!")

if __name__ == "__main__": 
    main()
