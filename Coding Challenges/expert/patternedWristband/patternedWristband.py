"""
Project

    A wristband can have 4 patterns:

    horizontal: each item in a row is identical.
    vertical: each item in each column is identical.
    diagonal left: each item is identical to the one on its upper left or bottom right.
    diagonal right: each item is identical to the one on its upper right or bottom left.
    You are shown an incomplete section of a wristband.

    Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.

Examples

    is_wristband([
    ["A", "A"],
    ["B", "B"],
    ["C", "C"]
    ]) ➞ True 
    # Part of horizontal wristband.

    is_wristband([
    ["A", "B"],
    ["A", "B"],
    ["A", "B"]
    ]) ➞ True 
    # Part of vertical wristband.

    is_wristband([
    ["A", "B", "C"],
    ["C", "A", "B"],
    ["B", "C", "A"],
    ["A", "B", "C"]
    ]) ➞ True
    # Part of diagonal left wristband.

    is_wristband([
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "B", "A"]
    ]) ➞ True
    # Part of diagonal right wristband.

Notes

    LINK: https://edabit.com/challenge/grorumaEjyFDmZQCx

Thoughts

    - input will be a list of lists, each sublist represents one row
    - check 4 patterns, horizontal, vertical, diagonal left, diagonal right.
        - if any are true. Return True. If all are false, return False.
    - horizontal
        - check each sublist. if all sublists contain same char return true
    - vertical
        - compare index i of each sublist.
    - diagonal left
        - compare element in (i + 1), (j + 1)
    - diagonal right
        - compare element in (i + 1), (j - 1)

"""

def is_wristband(lst):
    if(horizontalCheck(lst) == True):
        return(True)
    elif(verticalCheck(lst) == True):
        return(True)
    elif(diagonalLeft(lst) == True):
        return(True)
    elif(diagonalRight(lst) == True):
        return(True)
    return(False)

def horizontalCheck(lst):
    for i in range(len(lst)):
        prevItem = lst[i][0] # first item in row. Always compare to this item
        for j in range(len(lst[i])):
            if(prevItem != lst[i][j]): # if an item in the row is not equal to previous item
                return(False)
    return(True)

def verticalCheck(lst):
    for i in range(len(lst[0])):
        prevItem = lst[0][i] # topmost row, grab the item to the right every iteration
        for j in range(len(lst)):
            if(prevItem != lst[j][i]):
                return(False)
    return(True)

def diagonalLeft(lst):
    # need to compare left most & top most element to the row of elements right & down of current element.
    for i in range(len(lst[0])): # iterate through top row (go right)
        prevItem = lst[0][i]
        for j in range(len(lst)):
            try: # will be comparing some items that will be out of bounds, throw those results out.
                if(prevItem != lst[j][i + j]):
                    return(False)
            except:
                None
    for i in range(len(lst)): # iterate left most column (go down)
        prevItem = lst[i][0]
        for j in range(len(lst[i])):
            try:
                if(prevItem != lst[i + j][j]):
                    return(False)
            except:
                None
    return(True)

def diagonalRight(lst):
    # iterate through left most and bottom most, comparing to elements one up and one right of current element. Throw out all results with index < 0; python loops around when negative index.
    for i in range(len(lst[0])): # iterate through bottom row (go right)
        prevItem = lst[len(lst) - 1][i] # get item in bottom row, at index i
        tempIterator = 0
        for j in range(len(lst), -1, -1): # go from bottom, upwards
            try: 
                if(prevItem != lst[j][i + tempIterator]):
                    return(False)
                tempIterator += 1
            except:
                None
    for i in range(len(lst) - 1, -1, -1): # iterate left most column (go up)
        prevItem = lst[i][0]
        for j in range(len(lst[i])):
            try:
                if((i - j) < 0): # throw out all results with negative indexes (j cannot be negative). Can extend this, to avoid using try; except.
                    None
                elif(prevItem != lst[i - j][j]):
                    return(False)
            except:
                None
    return(True)

# # horizontal
# print(is_wristband([
#     ["A", "A"],
#     ["B", "B"],
#     ["C", "C"]
#     ]))

# # vertical
# print(is_wristband([
#     ["A", "B"],
#     ["A", "B"],
#     ["A", "B"]
#     ]))

# # diagonal left
# print(is_wristband([
#     ["A", "B", "C"],
#     ["C", "A", "B"],
#     ["B", "C", "A"],
#     ["A", "B", "C"]
#     ]))

# # diagonal right
# print(is_wristband([
#     ["A", "B", "C"],
#     ["B", "C", "A"],
#     ["C", "A", "B"],
#     ["A", "B", "A"]
#     ]))


# complete and tested July 30, 2023.