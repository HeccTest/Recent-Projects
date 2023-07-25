"""
Project

    Create a function that finds the highest integer in the list using recursion.

Examples

    find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

    find_highest([0, 12, 4, 87]) ➞ 87

    find_highest([8]) ➞ 8

Notes

    Please use the recursion to solve this (not the max() method).
    LINK: https://edabit.com/challenge/xRMQG4Sxewx5agDRr

Thoughts

    most straight forward method is to linearly go through the list removing the smallest value, calling the method again on the reduced list, and returning the result when there is one item in the list
        - this is inefficient and pointless though?
    
    will implement the idea above, as that seems to be the spirit of the challenge as opposed to efficiency.
"""


def find_highest(lst):
    minNum = lst[0] # var for keeping track of the smallest number in the list so far. Will remove this item at the end of the iteration. Stop if only one item remains
    if(len(lst) == 1): # base case (no error checking for empty list, not in the task)
        return(minNum)
    else: # recursion
        for i in range(len(lst)): # iterate through list linearly
            if(minNum > lst[i]): # if a number smaller than the current smallest is found in the list
                minNum = lst[i] # update minNum to be the smallest num found so far
        lst.remove(minNum) # removing the smallest number per execution
        return(find_highest(lst)) # recursively call the method, with new reduced list
        
print(find_highest([-1, 3, 5, 6, 99, 12, 2])) # testing

# completed and tested July 10, 2023
# Initially thought the project was rather redundant, and my solution to the question does make it seem so. However, checking online, there are better solutions that make the process more efficient. Still less efficient than a divide and conquer search, but more efficient than my solution!
