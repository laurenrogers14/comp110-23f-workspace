"""EX03 - Structured Wordle."""

__author__ = "730711512"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
string_secret: str = "codes"
string_guess: str = ""

def contains_char(any_length: str, single_character: str) -> bool:
    """Returns True if the single character is found at any index of the first string."""
    assert len(single_character) == 1
    # write a while loop going through each index of any_length.  if the single character matches any of these indexes, you can return True.
    index = 0
    while len(any_length) > index:
        if any_length[index] == single_character:
            return True
        index += 1
    return False

def emojified(string_guess: str, string_secret: str) -> str:
    """This function checks for correct emoji matches indices."""
    assert len(string_guess) == len(string_secret)
    emoji: str = ""
    string_guess_idx: int = 0
    while string_guess_idx < len(string_secret):
        if string_guess[string_guess_idx] == string_secret[string_guess_idx]:
            emoji += GREEN_BOX
        else: 
            word: bool = contains_char(string_guess, string_secret[string_guess_idx])
            if word is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        string_guess_idx += 1
    return emoji

        
def input_guess(expected_length: int) -> str:
    """Provide a guess of expected length"""
    user_input = input(f" Enter a {expected_length} character word:")
    string_secret: str
    while len(user_input) != expected_length:
        user_input = input(f" That wasn't {(expected_length)} chars! Try again: ")
    return user_input

def main() -> None:
    """The extry point of the program and main game loop."""
    # Your code will go here
    you_won = False
    count: int  = 1
    string_secret: str = "codes"
    while not you_won and count < 7:
        print(f"===Turn {(count)}/6 ===")
        string_guess == input_guess(len(string_secret))
        print(emojified(string_guess, string_secret))
        if string_guess == string_secret:
            print(f"you won in {(count)}/6 turns!")
            has_won = True
            exit
        count += 1
        if not you_won:
            print("X/6 -- Sorry, try again tomorrow!")       

if __name__ == "__main__": 
    main()
