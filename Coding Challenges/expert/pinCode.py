"""
Project

    Given a keypad that has the following layout:

    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘
    Your secret agent Mubashir has already given you a pincode. However, he also said it's possible that each of the digits he saw could be another adjacent digit (horizontally or vertically, but not diagonally).

    Suppose the secret agent has given you the code: 46:

    # Instead of the 4 it could also be 1, 5, or 7.
    # Instead of the 6 it could also be 3, 5, or 9.

    crack_pincode("46") ➞
    ["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]
    Create a function that takes an argument of pincode informed by your secret agent and returns a list of all possible variations of the pin codes.

Examples

    crack_pincode("0") ➞ ["0", "8"]

    crack_pincode("2") ➞ ["1", "2", "3", "5"]

    crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]

Notes

    - All pin codes must be strings, because of potentially leading 0s.

    LINK: https://edabit.com/challenge/mt4E3MYkoJASY8TE6

Thoughts

    - iterate through each digit in given order. Each digit will have between [1, 4] adjacent digits, meaning there will be [2,5] digits to test (including the given number)
    - how will I know which digits are adjacent?
        - maybe a dictionary, where each digit is the key, and the value will be a list of adjacent digits?
            - might not be the most efficient, but will start with this.

"""

def crack_pincode(pincode):
    adjPin = {
        "0" : ["0", "8"],
        "1" : ["1", "2", "4"],
        "2" : ["1", "2", "3", "5"],
        "3" : ["2", "3", "6"],
        "4" : ["1", "4", "5", "7"],
        "5" : ["2", "4", "5", "6", "8"],
        "6" : ["3", "5", "6", "9"],
        "7" : ["4", "7", "8"],
        "8" : ["0", "5", "7", "8", "9"],
        "9" : ["6", "8", "9"]
    }
    combinations = []
    possibleComb = 1 # total possible number of combinations
    for i in pincode:
        possibleComb *= len(adjPin[i]) # calculating total combinations

    # first string
    segmentCount = len(adjPin[pincode[0]])
    for j in range(segmentCount):
        for k in range(int(possibleComb / segmentCount)):
            combinations.append(adjPin[pincode[0]][j]) # making the initial list. Main reason first string is it's own execution

    # remaining string
    for i in pincode[1:]:
        segmentCount *= len(adjPin[i])
        for j in range(segmentCount):
            for k in range(int(possibleComb / segmentCount)):
                combinations[(j * int(possibleComb / segmentCount)) + k] += adjPin[i][j % len(adjPin[i])]
    return(combinations)
    
print(crack_pincode("01"))
print(crack_pincode("601"))
print(crack_pincode("007"))

# complete and tested July 27, 2023. Code is a little messy, would of liked to condense and make cleaner. Seems most online solutions are also using dictionary.