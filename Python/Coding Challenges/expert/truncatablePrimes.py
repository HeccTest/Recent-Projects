"""
Project

    A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.

    A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.

    Create a function that takes an integer as an argument and:

    - If the integer is only a left-truncatable prime, return "left".
    - If the integer is only a right-truncatable prime, return "right".
    - If the integer is both, return "both".
    - Otherwise, return False.

Examples

    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.

    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.

    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

    truncatable(5) ➞ "both"
    # The trivial case of single-digit primes is treated as truncatable from both directions.

    truncatable(139) ➞ False
    # 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

    truncatable(103) ➞ False
    # Because it contains a 0 digit (even though 103 and 3 are primes).

Notes


    - The input integers will not exceed 10^6. -> 1,000,000

    LINK: https://edabit.com/challenge/BfSj2nBc33aCQrbSg

Thoughts

    - "result is always prime" is unclear. It sounds like ALL results have to be prime, as in we will truncate until one digit remains. (sounds like recurssion)
    - a prime number is a whole number greater than one. I am going to assume input will be 0 or greater.
    - take given n, truncate left and check (recurssion). Then truncate right and check.
        - truncating using math may be overly compicated and thus more resource intensive. I will just convert to char, iterate through in order (depending on which direction i'm checking). Then convert back to int

"""
import math
def truncatable(n):
    leftTrunc = True
    rightTrunc = True
    nString = str(n)
    for i in range(len(nString)):
        if(isPrime(int(nString[0 : len(nString) - i])) == False): # trunc right
            rightTrunc = False
        if(isPrime(int(nString[i: len(nString)])) == False): # trunc left
           leftTrunc = False
        if(nString[i] == "0"): # if n contains a 0
            return(False)
    if(leftTrunc == True and rightTrunc == True):
        return("both")
    elif(leftTrunc == True):
        return("left")
    elif(rightTrunc == True):
        return("right")
    else:
        return(False)

def isPrime(x): # number is only divisible by 1 and itself
    # I could modulo x by every number between 2 and sqrt(x), but this is expensive. <-- USING THIS METHOD
    # alternatively, I could modulo x by every prime number between 2 and sqrt(x), this is less resource intensive, but messy as my list of prime numbers is fairly large

    if(x > 1):
        for i in range(1, math.trunc(math.sqrt(x))):
            if(x % (i + 1) == 0):
                return(False)
    else: # x is less than or equal to 1
        return(False)
    return(True)

print(truncatable(9137))

print(truncatable(5939))

print(truncatable(317))

print(truncatable(5))

print(truncatable(139))

print(truncatable(103))

# completed and tested July 25, 2023