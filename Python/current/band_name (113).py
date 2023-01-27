# https://replit.com/@makerdillon/BandNameGenerator1-Template?v=1
# ^ remix link, has a list of band names (txt file) as well as main file with comments on tasks that need to be completed.
import random
from tkinter.messagebox import YES

while True: # unconditional while loop (always run)
    print("Do you need a new band name?")
    userInput = input("Yes or No?\n--> ") # ask for input, provide a little text input area (decorative)
    if userInput.lower() == "yes":
        print("\nLet's find you one then!\n")
        break # breaking out of while loop
    else:
        print("\n" + userInput + "?\nI was expecting you to say yes!\nI'll ask again...\n")
        continue # continue statement returns to the beginning of the loop (it is redundant in this case, because our condtion (while True) is unconditional)

with open('C:/Users/Ryzen/Desktop/Python/current/bandNames.txt', 'r') as f: # opening a file in this file path (manually changed, because not in the default folder)
    bandNames = f.read().splitlines()

bandName = random.choice(bandNames)
print(bandName)