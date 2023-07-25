"""
Project

    The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

    Create a function that takes a string and applies the Atbash cipher to it.

Examples

    atbash("apple") ➞ "zkkov"

    atbash("Hello world!") ➞ "Svool dliow!"

    atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

Notes


    - Capitalisation should be retained.
    - Non-alphabetic characters should not be altered.

    LINK: https://edabit.com/challenge/MGALfBAXhXqqdFyqo

Thoughts

    - can convert char to ascii. Only consider a certain range (within alphabet), and apply some mathmatical shift to ascii value to correspond with the encryption

"""
encKey = {1:25, 2:23, 3:21, 4:19, 5:17, 6:15, 7:13, 8:11, 9:9, 10:7, 11:5, 12:3, 13:1,
          14:-1, 15:-3, 16:-5, 17:-7, 18:-9, 19:-11, 20:-13, 21:-15, 22:-17, 23:-19, 24:-21, 25:-23, 26:-25}
def atbash(txt):
    encryptedText = ""
    for i in txt:
        currChar = ord(i)
        if(currChar >= 65 and currChar <= 90): # if upper case letter  
            encryptedText += chr(currChar + encKey[currChar - 64])
        elif(ord(i) >= 97 and ord(i) <= 122): # if lower case letter
            encryptedText += chr(currChar + encKey[currChar - 96])
        else: # ignore, not an alphabet
            encryptedText += i
    return(encryptedText)

print(atbash("Christmas is the 25th of December"))

# complete and tested July 17, 2023