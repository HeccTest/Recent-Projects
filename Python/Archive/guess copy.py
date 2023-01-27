import math
import random
def setup():

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

print(list)

running = True
leftIndex = 0
rightIndex = len(list) - 1
i = 0
while(running == True):
    while(leftIndex <= rightIndex):
        mid = math.floor((leftIndex + rightIndex) / 2)
        if(list[mid] < guessNum):
            leftIndex = mid + 1
        elif(list[mid] > guessNum):
            rightIndex = mid - 1
        else:
            print("number found")
            running = False
            break
        i += 1 # visualize what is happening each iteration
        # print(i, ": ", mid, "\nlow: ", leftIndex, "\nHigh: ", rightIndex)
    if(running == True):
        guessNum = int(input("Guess Again: "))
    leftIndex = 0
    rightIndex = len(list) - 1
    