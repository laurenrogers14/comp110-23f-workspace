"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730711512"
 
word_chardle: str = input("Enter a 5-character word: ")

if len(word_chardle) != 5:
    print(" Error: Word must contain 5 characters. ")
    exit()
    
letter_chardle: str = input("Enter a single character: ")

if len(letter_chardle) != 1:
    print(" Error: Character must be a single character. ")
    exit()

count = 0
print(" Searching for " + letter_chardle + " in " + word_chardle)

if word_chardle[0] == letter_chardle:
    print(letter_chardle + " found at index 0 ")
    count += 1

if word_chardle[1] == letter_chardle:
    print(letter_chardle + " found at index 1 ")
    count += 1

if word_chardle[2] == letter_chardle:
    print(letter_chardle + " found at index 2 ")
    count += 1

if word_chardle[3] == letter_chardle:
    print(letter_chardle + " found at index 3 ")
    count += 1

if word_chardle[4] == letter_chardle:
    print(letter_chardle + " found at index 4 ")
    count += 1

print(str(count) + " instance of " + letter_chardle + " found in " + word_chardle) 

print(" No instances of " + letter_chardle + " found in " + word_chardle)