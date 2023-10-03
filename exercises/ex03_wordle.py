"""EX03 - Structured Wordle."""
__author__ = "730711512"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
string_secret: str = "codes"
string_guess: str = ""


def contains_char(string_secret: str, single_character: str) -> bool:
    """Returns True if the single character is found at any index of the first string."""
    assert len(single_character) == 1
    index: int = 0
    while index < len(string_secret):
        if (single_character == string_secret[index]):
            return True
        else:
            index = index + 1
    return False


def emojified(string_guess: str, string_secret: str) -> str:
    """This function checks for correct emoji matches indices."""
    assert len(string_guess) == len(string_secret)

    emoji: str = ""
    index: int = 0
    while index < len(string_secret):
        if string_secret[index] == string_guess[index]:
            emoji = emoji + GREEN_BOX
        else: 
            word: bool = contains_char(string_secret, string_guess[index])
            if word is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        index = index + 1
    return emoji

        
def input_guess(expected_length: int) -> str:
    """Provides a guess of the expected length."""
    string_guess = input(f" Enter a {expected_length} character word: ")
    while len(string_guess) != expected_length:
        string_guess = input(f" That wasn't {(expected_length)} chars! Try again: ")
    return string_guess


def main() -> None:
    """The extrypoint of the program and main game loop."""
    count = 1
    won = False


    while not won and count < 6:
        print(f"=== Turn {(count)}/6 ===")
        string_guess == input_guess(len(string_secret))
        print(emojified(string_guess, string_secret))
        if string_guess == string_secret:
            print(f"You won in {(count)}/6 turns!")
            won = True
            exit
        count = count + 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")       


if __name__ == "__main__": 
    main()
