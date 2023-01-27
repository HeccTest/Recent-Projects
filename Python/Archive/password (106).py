import random

weak_pass = input("Enter a password: ")
strong_pass = ""

for char in weak_pass:
    if(char.lower() == "e" or char == "3" ):
        options = ["3", "e", "E"] # an arrayList with three choices
        strong_pass += random.choice(options) # random.choice when given an arrayList like we have here will choose a random element in the list
    elif(char.lower() == "i" or char.lower() == "l"):
        options = ["1", "!", "i", "I", "l", "L"]
        strong_pass += random.choice(options)
    elif(char.lower() == "o" or char == "0"):
        options = ["o", "O", "0"]
        strong_pass += random.choice(options)
    else:
        strong_pass += char

print("Your secured password is:", strong_pass)

# this is the beginning of encryption.

# print(ord("h")) # will print the ascii value of h. we can apply changes to this integer number than convert it back to an ascii value.
# print(chr(104)) # will print the character represented by ascii value 104

# here is an ascii table: https://www.alpharithms.com/ascii-table-512119/





# here is a simple example (uncomment below to see)

# userInput = input("Enter a string: ")
# output = ""

# for char in userInput:
#     asciiVal = ord(char) + 3 # convert our character (a string that is one character long) into a integer value and add 3
#     output += chr(asciiVal) # add to our output string this mixed number

# print(output)



# # unscrambling
# userInput = input("would you like to unscramble? ")
# unscrambled = ""
# if userInput.lower() == "yes" or userInput.lower() == "y":
#     for char in output:
#         asciiVal = ord(char) - 3 # undo our + 3 from earlier. This (+3) can be seen as a encryption key
#         unscrambled += chr(asciiVal)
#     print(unscrambled)
# else:
#     print("output remains scrambled")