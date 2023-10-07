"""
Project

    Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples

    longest_substring("225424272163254474441338664823") ➞ "272163254"
    # substrings = 254, 272163254, 474, 41, 38, 23

    longest_substring("594127169973391692147228678476") ➞ "16921472"
    # substrings = 94127, 169, 16921472, 678, 476

    longest_substring("721449827599186159274227324466") ➞ "7214"
    # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
    # 7214 and 9274 have same length, but 7214 occurs first.

Notes


    - The minimum alternating substring size is 2, and there will always be at least one alternating substring.

    LINK: https://edabit.com/challenge/RB6iWFrCd6rXWH3vi

Thoughts

    - linearly iterate through string, character by character
        - may be more efficient to check if number is part of list (ie. ["0", "2", "4", "6", "8"]) rather than convert string to int and do an if check using modulo
    - keep track of longest substring so far, replacing when another substring of strictly greater length occurs. (same length is ignored, such that first instance will be returned)
    - since there will always be at least one alternating substring, I should not be expecting an empty string (will not catch an empty string)

"""

def longest_substring(digits):
    oddList = ["1", "3", "5", "7", "9"]
    longestSub = ""
    currSub = ""
    isOdd = None
    for i in digits:
        if(i in oddList): # curr num is odd
            if(isOdd == False): # prev num is even
                currSub += i
            else:
                currSub = i
            isOdd = True
        else: # curr num is even
            if(isOdd == True): # prev num is odd
                currSub += i
            else:
                currSub = i
            isOdd = False
        if(len(currSub) > len(longestSub)):
            longestSub = currSub
    return(longestSub)

print(longest_substring("721449827599186159274227324466"))

print(longest_substring("594127169973391692147228678476"))

print(longest_substring("225424272163254474441338664823"))


print(longest_substring("754388489999793138912431545258"), "545258") # failed this test, because the longest sub string is the last couple of digits. Need to change how I determine longest substring
# resolved by checking if currSub is longer than longestSub, every iteration (maybe there is a more efficient solution?)

# completed and tested July 20, 2023