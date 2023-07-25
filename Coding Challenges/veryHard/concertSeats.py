"""
Project

    Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

    Everyone can see the front-stage in the example below:

    # FRONT STAGE
    [[1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 2, 2],
    [5, 5, 5, 5, 4, 4],
    [6, 6, 7, 6, 5, 5]]

    # Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
    # 6 > 5 > 4 > 2 - so all numbers can see, etc.
    Not everyone can see the front-stage in the example below:

    # FRONT STAGE
    [[1, 2, 3, 2, 1, 1], 
    [2, 4, 4, 3, 2, 2], 
    [5, 5, 5, 10, 4, 4], 
    [6, 6, 7, 6, 5, 5]]

    # The 10 is directly in front of the 6 and blocking its view.
    The function should return True if every number can see the front-stage, and False if even a single number cannot.

Examples

    can_see_stage([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]) ➞ True

    can_see_stage([
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
    ]) ➞ True

    can_see_stage([
    [2, 0, 0], 
    [1, 1, 1], 
    [2, 2, 2]
    ]) ➞ False

    can_see_stage([
    [1, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
    ]) ➞ False

    # Number must be strictly smaller than 
    # the number directly behind it.

Notes


    - Numbers must be strictly greater than the number in front of it.
    - All numbers within the lists will be whole numbers greater than or equal to zero.

    LINK: https://edabit.com/challenge/xbjDMxzpFcsAWKp97

Thoughts

    - input looks to be a list of equal length lists. This means concert rows have an equal amount of seats
        - if rows can have variable number of seats, I may run into a null pointer error
    - most straight forward solution that comes to mind is a nested linear check:
        - iterate through the rows
        - check each row behind
    - first couple rounds of comparisons in a linear approach would look like this:
        seats[0][0]
        seats[1][0]

        seats[1][0]
        seats[2][0]

"""


def can_see_stage(seats):
    # ASSUMING ALL ROWS HAVE AN EQUAL NUMBER OF SEATS
    for i in range(len(seats[0])): # iterate through a row (horizontal)
        for j in range(len(seats) - 1): # iterate through each row (vertical)
            if(seats[j][i] >= seats[j + 1][i]): # if seat in front is obstructing view
                return(False)
    return(True)

    

print(can_see_stage([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]))

print(can_see_stage([
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
    ]))

print(can_see_stage([
    [1, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
    ]))

# completed and tested July 18, 2023

"""
    lots of the online solutions use zip() - https://www.w3schools.com/python/ref_func_zip.asp
    I could use this to create new lists that have direct correlation to the other items in the same list. But, I don't think this solution would be any faster in terms of run time?
    - it could potentially solve for when an unequal number of seats per row is presented.
"""