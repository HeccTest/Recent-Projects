"""
Project

    This challenge is based on the classic videogame "Snake".

    Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

    In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

    Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.

Examples

    snakefill(3) ➞ 3

    snakefill(6) ➞ 5

    snakefill(24) ➞ 9

Notes

    The given number will always be a positive integer (there are no exceptions to handle).
    LINK: https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt

Thoughts

    - total area = n^2
    - if snakeLength >= total area, output the amount of times the snake has eaten - 1

"""

def snakefill(n):
    eatCount = 0
    snakeLength = 1
    while(snakeLength <= (n * n)): # while the snake does not cover the entire board yet, eat once. Do until snake length exceeds the board size.
        snakeLength += snakeLength
        eatCount += 1
    return(eatCount - 1)

print(snakefill(3))

print(snakefill(6))

print(snakefill(24))

# completed and test July 15, 2023