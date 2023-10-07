"""
Project

    You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

Examples

    n = 4
    4 is 0100 in binary. We are working in 32 bits so:
    00000000000000000000000000000100 = 4
    11111111111111111111111111111011 = 4294967291
    return 4294967291

    
    flipping_bits(2147483647) ➞ 2147483648
    01111111111111111111111111111111
    10000000000000000000000000000000

    flipping_bits(1) ➞ 4294967294

    flipping_bits(4) ➞ 4294967291

Notes

    N/A
    LINK: https://edabit.com/challenge/z39yXccJGLAy3BDNX

Thoughts

    - 32 bit unsigned. We are working strictly in positive numbers, between 0 to 2^32
    - input will be an integer. I have to convert to binary (or at least simulate), then flip ALL bits.
    - 2^32 is 4,294,967,296 (so, we can represent from 0 to 4,294,967,295)

    - can use str.format to convert to binary string: "{0:032b}".format(4), also can add 0 in front as necessary to accurately represent 32 bit.

"""

def flipping_bits(n):
    givenBits = "{0:032b}".format(n) # store the given bits as a string of 0's and 1's in a 32bit format.
    reversedBits = "" # empty string to hold the flipped bits
    for i in givenBits:
        if(i == "0"):
            reversedBits += "1"
        elif(i == "1"):
            reversedBits += "0"
    return(int(reversedBits, 2)) # cast my string of base 2 (binary) numbers into an integer


# TESTING

print(flipping_bits(2147483647))

print(flipping_bits(1))

print(flipping_bits(4))

# complete and tested July 15, 2023

"""
some of the online solutions did not interact with binary bits at all and instead just subtracted from the integer value, ie.

def flipping_bits(n):
	return 4294967295 - n

This is an interesting solution, as it solves the problem at hand far better (resource wise).
For the future - read the notes carefully, and if there is no preference towards a specific method of solving the issue. Take the easiest and fastest solution. (albeit I didnt think to just subtract from (2^32 - 1) - n)
"""