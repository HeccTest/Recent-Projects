"""
Project

    Create a function that takes a number num and returns its length.

Examples

    number_length(10) ➞ 2

    number_length(5000) ➞ 4

    number_length(0) ➞ 1
Notes

    The use of the len() function is prohibited.
    LINK: https://edabit.com/challenge/2zKetgAJp4WRFXiDT

Thoughts

    convert to string, then iteration through str to find number of characters
"""

# count = 0
# for i in ("test"):
#     count += 1
# print(count)

def number_length(num):
    count = 0
    for i in (str(num)):
        count += 1
    return(count)

# completed and tested July 14, 2023