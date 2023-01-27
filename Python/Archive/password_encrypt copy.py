userInput = input("Enter a password: ") # password
userOutput = ""

for char in userInput:
    value = ord(char) # ord(char) returns the ascii decimal value of char
    value += 3

    userOutput += (chr(value))

print(userOutput)


decrypt = ""
key = input("enter a decryption key: ")
for char in userOutput:
    value = ord(char) # ord(char) returns the ascii decimal value of char
    value -= int(key)

    decrypt += (chr(value))

print(decrypt)