"""
Project

    A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

    [1, 1, 0, 0, 0, 1, 0]
    Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. You are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

    So, if we use the example above:

    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 1st cell.

    [0, 0, 1, 1, 1, 0, 1] 
    # You free the prisoner in the 3rd cell (2nd one locked).

    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

    [0, 0, 1, 1, 1, 0, 1]
    # You free the prisoner in the 7th cell - and you are done!
    Here, we have set free 4 prisoners in total.

    Create a function that, given this unique prison arrangement, returns the number of freed prisoners.

Examples

    freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4

    freed_prisoners([1, 1, 1]) ➞ 1

    freed_prisoners([0, 0, 0]) ➞ 0

    freed_prisoners([0, 1, 1, 1]) ➞ 0

Notes


    - You are the prisoner in the first cell. You must be freed to free anyone else.
    - You must free a prisoner in order for the locks to switch. So in the second example where the input is [1, 1, 1] after you release the first prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners.
    - You always start within the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.

    LINK: https://edabit.com/challenge/SHdu4GwBQehhDm4xT

Thoughts

    - think there is some ambiguity: Do I have to free prisoners in order from left to right, or starting from the left, free as many assuming I can only go right?
        - I am going to assume the first - I must go in order from left to right, and always free when possible, simply because this is easier.
        - not sure it ever makes sense to do the latter anyway. Do not think I can free more prisoners using the second strategy?
    - every step I take (every prisoner freed), I have to simulate a binary flip
        - worst case, I linearly iterate through list from current position, and flip the bits to the right.
        - alternatively, I could just have two lists: one being the original, and the other being the flipped. Choose which list to look at depending on number of prisoners freed (at least better run time than solution above)

"""

def freed_prisoners(prison):
    if(prison[0] == 0): # I am in a locked cage :c
        return(0)
    else:
        flippedPrison = []
        for i in range(len(prison)):
            if(prison[i] == 0):
                flippedPrison.append(1)
            else:
                flippedPrison.append(0)
        playerPointer = 0
        prisonersFreed = 0
        while(playerPointer < len(prison)):
            if(prisonersFreed % 2 == 0): # even number of prisoners freed so far (use prison)
                if(prison[playerPointer] == 1):
                    prisonersFreed += 1
            else:
                if(flippedPrison[playerPointer] == 1):
                    prisonersFreed += 1
            playerPointer += 1
        return(prisonersFreed)

print(freed_prisoners([0, 1, 1, 1]))

print(freed_prisoners([1, 1, 1]))

print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))

# completed and test July 19, 2023