"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730711512"

word: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")

if word[0] == letter:
    print(letter + " found at index 0")

if word[1] == letter:
    print(letter + " found at index 1")

if word[2] == letter:
    print(letter + " found at index 2")

if word[3] == letter:
    print(letter + " found at index 3")

if word[0] == letter:
    print(letter + " found at index 0" + "1 instance of e found in word")
else:
    print( "No instances of" + letter +  " found in word.")

if word[1] == letter:
    print(letter + " found at index 1" + "1 instance of e found in word")
else:
    print( "No instances of" + letter +  " found in word.")

if word[2] == letter:
    print(letter + " found at index 2" + "1 instance of e found in word")
else:
    print( "No instances of" + letter + " found in word.")

if word[3] == letter:
    print(letter + " found at index 3" + "1 instance of e found in word")
else:
    print( "No instances of" + letter + " found in word.")


