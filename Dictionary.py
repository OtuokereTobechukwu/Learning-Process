 # A simple dictionary program
# Author - Otuokere Tobechukwu
# -------------------------------------------------------

# importing libraries
import json
from difflib import get_close_matches

# Load the data
data = json.load(open("2.1 data.json.json"))


# A simple function to search for  the word in the Json dataset
def wordsearch(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        choice = input(
            "Did you mean %s instead? If yes, press Y and if No, press N:" % get_close_matches(w, data.keys())[
                0]).lower()
        if choice == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif choice == "n":
            return "This is not a word! Please double check"
        else:
            return "I don't understand sir!"
    else:
        return "This word cannot be found! Please enter an English word."


# User input
word = input("Enter a word: ")
definition = wordsearch(word)
# Printing out the results
if type(definition) == list:
    for defs in definition:
        print(defs)
else:
    print(definition)
