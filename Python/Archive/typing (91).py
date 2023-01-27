import time
import random

totalTime = 0
playing = True

print("welcome to the Typing Game! How fast can you type?") # Formatting
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("GO!")

startTime = time.time()

words = open("words.txt").read().splitlines() # Open text file: 'words.txt'. read() takes the entire file. splitlines() makes a list of words seperated by space or newline

for turn in range(5):
    print() # Formatting
    print("TURN NUMBER:", turn + 1, "OF 5")
    word = random.choice(words) # choice() is a method in the random library. It chooses an element of the given sequence (in this case the list words)
    print("word:", word)

    correct = False

    while(correct == False):
        attempt = input("> ") # Formatting
        if(attempt == word):
            correct = True # breaks out of this while loop once we type the correct word. Goes back into the for loop
        else:
            print("Try again!") # this while loop runs again

endTime = time.time()
totalTime = endTime - startTime

print()
print("CONGRATULATIONS")
print("Your Time:", round(totalTime, 1), "Seconds")