"""
Project

    Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.

    Attributes
    An instance of the class Sudoku will have one attribute:

    board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
    Methods
    An instance of the class Sudoku wil have three methods:

    get_row(n): will return the row in position n.
    get_col(n): will return the column in position n.
    get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.

Examples

    **THERE IS A PICTURE OF THE BOARD AT THE LINK IN NOTES**

    game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

    game.board ➞ [
    [4, 1, 7, 9, 5, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 6, 0, 0, 0, 7, 0, 0, 0],
    [0, 5, 0, 0, 0, 9, 1, 0, 6],
    [8, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 4, 0, 0],
    [9, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 0, 0, 0],
    [2, 0, 0, 7, 0, 1, 5, 8, 0]
    ]

    game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
    game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
    game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
    game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
    game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

Notes

    - All positions are indexed to 0.
    - All orders are assigned left to right and top to bottom.

    LINK: https://edabit.com/challenge/CMDy4pvnTZkFwJmmx

Thoughts

    - have to make the following functions:
        - board()
            - return the entire board
        - get_row(n)
            - return the nth row
            - just return board[n]
        - get_col(n)
            - return the nth column
            - linearlly iterate through each row returning board[0 ... 8][n]
        - get_square([n, m])
            - return the square at given location. Where n = row, and m = col.
            - m is optional. When m is not given n will instead determine the square number. n will be in range [0,8]

"""

class Sudoku:
    # constructor: convert given string into a board; a list holding 9 lists, each representing one row.
    def __init__(self, gb):
        self.givenBoard = []
        tempRow = []
        for i in gb:
            tempRow.append(int(i))
            if(len(tempRow) == 9):
                self.givenBoard.append(tempRow)
                tempRow = []
            
    def board(self):
        return(self.givenBoard)
    
    def get_row(self, n):
        return(self.givenBoard[n])
    
    def get_col(self, n):
        outputCol = []
        for i in range(9):
            outputCol.append(self.givenBoard[i][n])
        return(outputCol)
    
    def get_sqr(self, n, m = -1):
        outputSqr = []
        if(m > -1): # given a column, n represents row number
            targetRow = int(n / 3)
            targetCol = int(m / 3)
            for i in range((targetRow * 3), ((targetRow * 3) + 3)):
                for j in range((targetCol * 3), ((targetCol * 3) + 3)):
                    outputSqr.append(self.givenBoard[i][j])
        else: # no column. n represents square number, rather than row.
            targetRow = int(n / 3) # determines which section of the board we are looking at. top, middle, or bottom
            targetCol = n % 3 # determines board left, middle, or right
            for i in range((targetRow * 3), ((targetRow * 3) + 3)):
                for j in range((targetCol * 3), ((targetCol * 3) + 3)):
                    outputSqr.append(self.givenBoard[i][j])
        return(outputSqr)
    
# completed and tested July 29, 2023. See testingSudokuParser.py for test cases.