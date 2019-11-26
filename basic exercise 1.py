# A program to cover different operational constructs in python.

# Creating a variable to hold an empty list
sentences = []


# Creating a function to capitalize
def titles(word):
    translation = word.capitalize()
    return translation


# This iterates until the secret word has been entered and thereafter, appends the words to the sentences list
while True:
    statement = input("Say something: ")
    if statement == "\end":
        break
    else:
        sentences.append(statement)

# Looping through the sentences list and capitalizing.
for phrases in sentences:
    trans = titles(phrases)
    print(trans)
