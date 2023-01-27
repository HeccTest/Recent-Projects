import time
import random

totalTime = 0
playing = True

print("Welcome to the Typing Game! How fast can you type?")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("GO!")

startTime = time.time()

words = open("words.txt").read().splitlines()

for turn in range(5):
    print()
    print("TURN NUMBER:", turn + 1, "OF 5")
    word = random.choice(words)
    print("word:", word)

    correct = False

    while(correct == False): # while the user has not guessed the correct word
        attempt = input("> ") # formatting
        if(attempt == word):
            correct = True
        else:
            print("Try Again!")

endTime = time.time()
totalTime = endTime - startTime

print()
print("CONGRATULATIONS!")
print("Your time:", round(totalTime, 2), "seconds")