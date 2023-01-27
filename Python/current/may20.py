#Modules
import random

#Asking the user if they want a band name
print("Do you need a new band name?")
userIn = input("Yes or No?\n--> ")

while True: # unconditional truth statement (infinite loop)
    if(userIn.lower() == "yes"):
        break # breaking out of the unconiditonal while loop (moving onto next step)
    else:
        print("\n" + userIn + "?\nI was expecting you to say yes!")
        print("\nI'll ask again\n")

        print("Do you need a new band name?")
        userIn = input("Yes or No?\n--> ")

#Importing a list of band names
with open('current/bandNames.txt', 'r') as file: # open file from relative path as read
    bandNames = file.read().splitlines() # read the file (bandNames.txt), splitting each item into an arrayList everytime a newline is read

print("\nLet's find you one then!\n")
print("Randomizing...\n\n...\n")
print("Some band name options are...\n")

bandName1 = random.choice(bandNames)
bandName2 = random.choice(bandNames)
bandName3 = random.choice(bandNames) # no prevention of duplicate band names rn

#Returning some options

print(bandName1)
print(bandName2)
print(bandName3 + "\n")

while True:
    userIn = input("Which one do you like? 1, 2, or 3? Type anythin else for more options\n--> ")
    if(userIn == "1"):
        chosenName = bandName1
        break
    elif(userIn == "2"):
        chosenName = bandName2
        break
    elif(userIn == "3"):
        chosenName = bandName3
        break
    else: # reroll band names
        print("\nRandomizing...\n\n...\n")
        print("Some band name options are...\n")

        bandName1 = random.choice(bandNames)
        bandName2 = random.choice(bandNames)
        bandName3 = random.choice(bandNames) # no prevention of duplicate band names rn

        #Returning some options

        print(bandName1)
        print(bandName2)
        print(bandName3 + "\n")

#Print new band name
print("\nYour new band Name is...\n")
print(chosenName)
print("\nThat's a cool name!")
print("\nCan you come up with a better band Name?\n")
userIn = input("Yes or No?\n--> ")

#Creating an original band name
while True:
    if(userIn.lower() == "yes"):
        userIn = input("\nWhat is it then?\n\n--> ")
        chosenName = userIn # set the chosenName to custom user name
        customName = True # user made a custom name
        break
    elif(userIn.lower() == "no"):
        customName = False # user did not make a custom name
        break # break out of loop, skip straight to rating
    else:
        userIn = input("Yes or No?\n--> ") # user error (answer != yes or no)

#Rating your band name (Bonus)
# rate the name regardless if customName or not, arbitrary rating system
if(customName == True): # user chose a custom name
    print("\n")
else: # user did not choose a custom name
    print("I thought that one was good too!\n")


if(len(chosenName) < 5):
    score = str(len(chosenName) % 5) # max score of 5 for short names
else:
    score = str(len(chosenName) % 10) # max score of 10 for longer ( < 5 ) names
print("We give your band name, " + chosenName + ", a rating of " + score + " out of ten")
print("That is a great Name!")


#Adding band name to the list (Advanced)




#print("\n\nWe Love You\n",bandName,"\nYou ROCK!!")