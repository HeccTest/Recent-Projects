"""
Project

    Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples

    area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

    area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

    area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"
Notes

    The total world's landmass is 148,940,000 [Km^2]
    Round the result to two decimal places.
    If you get stuck on a challenge, find help in the Resources tab.
    LINK: https://edabit.com/challenge/Cjtm4CpLzHDerQMfX

Thoughts

    - given land mass / total land mass
    - convert to percentage (shift decimals)
    - Format to two decimal places
    - Output final result
"""

def area_of_country(name, area):
    return(name + " is " + "%.2f" % (area / 148940000 * 100) + "% of the total world's landmass")

print(area_of_country("USA", 9372610))

print(area_of_country("Iran", 1648195))

# complete and test July 14, 2023

"""
def area_of_country(name, area):
    return "{} is {:.2%} of the total world's landmass".format(name, area / 148940000)

The online solution uses string.format to solve with fewer steps.
- consider using str.format() in the future
- https://www.w3schools.com/python/ref_string_format.asp
"""