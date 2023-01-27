import random
import time

def bubbleSort(): # https://en.wikipedia.org/wiki/Bubble_sort
    bubbleList = rList.copy()
    for i in range (len(bubbleList)): # 0 -> 9. Not the most efficient. will always have worst case run time
        for j in range(len(bubbleList) - 1 - i): # 0 -> (8 - i)
            left = bubbleList[j]
            right = bubbleList[j + 1]

            if(left > right): # if left > right then I want to swap
                bubbleList[j + 1] = left
                bubbleList[j] = right

            # if right > left then I do nothing
            # if right == left then I can also do nothing

    print("BUBBLE SORT: ")
    print(bubbleList)

def insertionSort(): # https://en.wikipedia.org/wiki/Insertion_sort USING ONLINE SOLUTION: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    insertionList = rList.copy()
    for i in range (1, len(insertionList)): # iterate through the list ignoring the first element (because the first element will be part of our solved list)
        key = insertionList[i] # the element of focus for this iteration

        j = i-1 # j is the previous element; initially it is the element before i
        while j >= 0 and key < insertionList[j] : # while j is within range and our key is still smaller then the previous element
                insertionList[j+1] = insertionList[j] # move j down the list (this will replace an element, but will be balanced out once we place the key)
                j -= 1
        insertionList[j+1] = key # once we find a place where key is the largest element

    print("Insertion Sort: ")
    print(insertionList)


rList = []

for n in range(10): # n numbers in our list
    rList.append(random.randint(1, 1000)) # duplicate values possible


print("RANDOM LIST: ")
print(rList)
print() # formatting

bubbleStart = time.time()
bubbleSort()
print("Bubble sort took: " + (str)(round((time.time() - bubbleStart), 4))) # small example will take practically 0 time
print() # formatting

insertionStart = time.time()
insertionSort()
print("Insertion sort took: " + (str)(round((time.time() - insertionStart), 4))) # small example will take practically 0 time