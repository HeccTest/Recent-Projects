"""
Project

    Create a function that takes a list representation of a Minesweeper board, and returns another board where the value of each cell is the amount of its neighbouring mines.

Examples

    The input may look like this:

    [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0]
    ]
    The 0 represents an empty space . The 1 represents a mine.

    You will have to replace each mine with a 9 and each empty space with the number of adjacent mines, the output will look like this:

    [
        [1, 9, 2, 1],
        [2, 3, 9, 2],
        [3, 9, 4, 9],
        [9, 9, 3, 1]
    ]

Notes


    - Since in the output the numbers 0-8 are used to determine the amount of adjacent mines, the number 9 will be used to identify the mines instead.
    - A wikipedia page explaining how Minesweeper works is available in the Resources tab.

    LINK: https://edabit.com/challenge/v2eHXTn2qobw2WYJP

Thoughts

    - since the notes specify 0 - 8 are used to represent neighbouring mines. This means a mine diagonal from current position is counted as adjacent (see bottom right of grid)
    - will have to process a board of unspecified size.
        - input is a list of lists containing ints [0, 1]
        - each position will need to check 8 other positions? (this would probably be worst case)
            - the edges will have different interactions. I can't check the number on the left of [0, 0], that would get index out of bounds
            - maybe use try catch instead
                - when using a try, catch. If an index is out of bounds, no error will be thrown (in our use case). However, we will exit the try catch, stopping the code short.
                    - if our check needs to be so stringent, we may as well not use try - catch, since at this point the inputs will not have any index out of bounds errors.
            - need to check [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
                - Do not need to check [i, j]. That is current pointer. Although it does not hurt to just gloss over it.
                - can check in any order
            - python accepts board[-1][0] as to mean go the last item in the list and grab the first thing from that list. This is problematic for our method.
    - will assume each row will have the same length

"""

def minesweeper_numbers(board):
    outputList = []
    row = []
    nearbyMines = 0
    for i in range(len(board)):
        for j in range(len(board[0])): # assuming every row is of equal length
            if(board[i][j] == 1): # if current position is a mine. Replace with value 9
                row.append(9)
            else: # not a mine, need to figure out how many mines adjacent
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if((i + a) >= 0 and (i + a) < len(board) and (j + b) >= 0 and (j + b) < len(board[0])): # filter out any index out of bounds
                            if(board[i + a][j + b] == 1): # there is a mine nearby
                                nearbyMines += 1
                row.append(nearbyMines)
                nearbyMines = 0
        outputList.append(row)
        row = []
    return(outputList)


print(minesweeper_numbers([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0]
    ]))

# completed and tested July 23, 2023