def encode(key, msg):
    encodedMsg = ""
    for i in range(len(msg)):
        if(ord(msg[i]) + int(key) > 126): # if the encoded character exceeds ascii limits (we will just loop around)
            encodedMsg += (chr(ord(msg[i]) + int(key) - 126 + 32))
        else:
            encodedMsg += (chr(ord(msg[i]) + int(key)))
    print("Message: " + encodedMsg)
    print("Key: " + key)


def decode(key, msg):
    decodedMsg = ""
    for i in range(len(msg)):
        if(ord(msg[i]) - int(key) < 32):
            decodedMsg += (chr(ord(msg[i]) - int(key) + 126 - 32))
        else:
            decodedMsg += (chr(ord(msg[i]) - int(key)))
    print("Message: " + decodedMsg)
    print("Key: " + key)

userIn = ""
while(userIn.casefold() != "q" and userIn.casefold() != "exit" and userIn.casefold() != "quit"): # infinite loop until quit
    userIn = input("Encode (e) or Decode (d)?\n> ")
    if(userIn.casefold() == "e" or userIn.casefold() == "encode"): # casefold ignores case
        userMsg = input("Enter a message\n> ")
        userKey = input("Enter a key (Int)\n> ")
        encode(userKey, userMsg)
    elif(userIn.casefold() == "d" or userIn.casefold() == "decode"):
        userMsg = input("Enter an encrypted message\n> ")
        userKey = input("Enter a key (Int)\n> ")
        decode(userKey, userMsg)


