"""
Project

    Given two strings, that may or may not be of the same length, determine the minimum number of character deletions required to make an anagram. Any characters can be deleted from either of the strings.

Examples

    make_anagram("cde", "abc") ➞ 4
    # Remove d and e from cde to get c.
    # Remove a and b from abc to get c.
    # It takes 4 deletions to make both strings anagrams.

    make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") ➞ 30

    make_anagram("showman", "woman") ➞ 2

Notes

    LINK: https://edabit.com/challenge/Sws7TmBqGJZfReepJ

Thoughts

    - anagram: a word or phrase made by transposing the letters of another word or phrase
        - seems they have to be equal length in this case. See ("showman", "woman"), "woman" would already be an anagram otherwise.
    - can delete from either string.
        - does it make sense to always delete from longer string..?
            - no. Have to delete all chars the strings do not have in common
    - alternatively. Since I do not need to output the resulting strings. Just the minimal number of removals.
        - I could find the intersection between string a and b; how many chars they have in common
        - subtract common chars from a and b. The subtracted amounts becomes my output.
    - there doesn't seem to a case for when there is no possible anagrams

"""

def make_anagram(a, b):
    commonChars = 0
    bLength = len(b)

    # comparing string a to string b
    for i in a:
        jCount = 0
        for j in b:
            if(i == j): # remove chars the strings have in common
                b = b[:jCount] + b[jCount + 1:]
                commonChars += 1
                break # break out of for j loop. I do not want char i to be compared again
            jCount += 1
    return((len(a) - commonChars) + (bLength - commonChars))

# complete and tested Aug 1, 2023. See test_MakeAnagram.py for test cases, and results.