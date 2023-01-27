import math
import random
def setup(): # you can ignore this

    sList = []
    while(len(sList) <= 20): # adds 20 elements to the list
        rNum = random.randint(1,100) # each element is between 1 and 100
        if(rNum not in sList): # prevents duplicates
            sList.append(rNum)

    for i in range (len(sList)):
        for j in range(len(sList) - 1 - i):
            left = sList[j]
            right = sList[j + 1]

            if(left > right):
                sList[j + 1] = left
                sList[j] = right
    return sList
list = setup() # a list of sorted numbers

guessNum = int(input("Guess a number between 1 and 100: ")) # the user's guess

# Win Condition: The user's guess is in the list
# https://en.wikipedia.org/wiki/Binary_search_algorithm
numberFound = False # tells me if the number is found (user's guess is in my list). Used to determine if game is over

lowIndex = 0
highIndex = len(list) - 1
print(list)
i = 0
while(numberFound == False):
    while (lowIndex <= highIndex):
        mid = math.floor((lowIndex + highIndex) / 2)
        if(list[mid] < guessNum):
            lowIndex = mid + 1
        elif(list[mid] > guessNum):
            highIndex = mid - 1
        else: # if the number is found
            print("Number found at index: ", mid)
            numberFound = True
            break # break out of the binary search (the inner while loop), the game continues
        i += 1 # visualize what is happening each iteration (uncomment out the next line as needed)
        # print(i, ": ", mid, "\nlow: ", lowIndex, "\nHigh: ", highIndex)

    # if the number is not found I will reset the left and right index and ask the user to guess again
    lowIndex = 0
    highIndex = len(list) - 1
    i = 0
    if(numberFound == False): # if the user has not guessed correctly yet
        guessNum = int(input("Guess again (1 - 100): ")) # Have the user guess again

