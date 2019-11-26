# Basic file reading
myfile = open("example.txt")
print(myfile.read())

# Cursor concept
# This just enable you print the text file as many times as you want because you have saved the content in a variable
myfile = open("example.txt")
content = myfile.read()
print(content)

# Applying the close method implicitly
with open("example.txt") as myfile1:
    content1 = myfile1.read()

print(content1)

# Writing text to a file.
with open("example2.txt", "w") as newfile:
    newfile.write("Agbalumo")

# Appending text to an existing file.
with open("example2.txt", "a") as newfile:
    newfile.write("Agbalumoq")

