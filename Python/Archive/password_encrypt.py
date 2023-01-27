userInput = input("Enter a password: ") # password
userOutput = ""

for char in userInput:
    if char.lower() == "e":
        userOutput += "3"
    elif char.lower() == "a":
        userOutput += "@"
    elif char.lower() == "i":
        userOutput += "!"
    else:
        userOutput += char
        # userOutput += char  === userOutput = userOutput + char

print(userOutput)