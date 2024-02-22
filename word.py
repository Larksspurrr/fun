from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, digits, punctuation
from time import sleep

lower_letters = [letter for letter in lowercase]
upper_letters = [letter for letter in uppercase]
numbers = [num for num in digits]
symbols = [symbol for symbol in punctuation]
lists = [lower_letters, upper_letters, numbers, symbols]

input_string = input("Word: ")
string = ""
index = 0

while string != input_string:
    active_list = lower_letters
    for character in input_string:
        for set_list in lists:
            if character in set_list:
                active_list = set_list
                break
        for letter in active_list:
            if character == " ":
                string += " "
                break
            sleep(.05)
            string = string[:index] + letter
            print(string)
            if letter == character:
                break
        index += 1