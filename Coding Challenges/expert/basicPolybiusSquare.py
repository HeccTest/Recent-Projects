"""
Project

    The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).

        1	2	3	4	5
    1	A	B	C	D	E
    2	F	G	H	I/J	K
    3	L	M	N	O	P
    4	Q	R	S	T	U
    5	V	W	X	Y	Z

    To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

    Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.

Examples

    polybius("Hi") ➞ "2324"

    polybius("2324  4423154215") ➞ "hi there"

    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

Notes

    As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).

    LINK: https://edabit.com/challenge/2C3gtb4treAFyWJMg

Thoughts

    - j is inaccessible. 24 will always return i. And j will always be converted into 24.
    - when given an input, need to differentiate between numbers and text. Input will always be string
        - when given numbers, need to group together 2 numbers (representing row, column)
    - might be most effecient to simply do a dictionary lookup?
    - from test notes: DISREGARD PUNCTUATION, BUT KEEP SPACES!

"""

def polybius(text):
    # if the first character's ascii value is less than 58; the entire string consists of digits.
    if(ord(text[0]) < 58):
        return(decipher(text))
    else:
        return(encipher(text))
    
# convert words into numbers
def encipher(text):
    encipherDict = {
        "a" : "11",
        "b" : "12",
        "c" : "13",
        "d" : "14",
        "e" : "15",
        "f" : "21",
        "g" : "22",
        "h" : "23",
        "i" : "24",
        "j" : "24",
        "k" : "25",
        "l" : "31",
        "m" : "32",
        "n" : "33",
        "o" : "34",
        "p" : "35",
        "q" : "41",
        "r" : "42",
        "s" : "43",
        "t" : "44",
        "u" : "45",
        "v" : "51",
        "w" : "52",
        "x" : "53",
        "y" : "54",
        "z" : "55",
        " " : " "
    }

    encipheredText = ""
    for i in text.lower():
        try:
            encipheredText += encipherDict.get(i)
        except: # throws out anything that is not in dictionary. Primarily punctuation
            None
    return(encipheredText)

# convert numbers into words
def decipher(text):
    decipherDict = {
        "11" : "a",
        "12" : "b",
        "13" : "c",
        "14" : "d",
        "15" : "e",
        "21" : "f",
        "22" : "g",
        "23" : "h",
        "24" : "i",
        "25" : "k",
        "31" : "l",
        "32" : "m",
        "33" : "n",
        "34" : "o",
        "35" : "p",
        "41" : "q",
        "42" : "r",
        "43" : "s",
        "44" : "t",
        "45" : "u",
        "51" : "v",
        "52" : "w",
        "53" : "x",
        "54" : "y",
        "55" : "z"
    }

    decipheredText = ""
    currentKey = ""
    for i in text:
        if(i == " "):
            decipheredText += " "
        # if next char is a number, add to currentKey until 2 numbers. Then dictionary look up, and reset.
        else:
            currentKey += i
            if(len(currentKey) > 1):
                decipheredText += decipherDict.get(currentKey)
                currentKey = ""
    return(decipheredText)


# completed and tested Aug 2. 2023, see test_basicPolybiusSquare.py for test cases