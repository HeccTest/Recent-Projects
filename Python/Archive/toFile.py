# open("file name", "read, write, or append")

# with open("test.txt", "w") as file:
#     file.write("Hello World!")

# with open("test.txt", "a") as file:
#     file.write("Hello World!")

with open("test.txt", "r") as file:
    content = file.read()

print("the file contained: " + content)