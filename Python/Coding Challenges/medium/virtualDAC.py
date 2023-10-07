"""
Project

    Create a function that takes a decimal number representation of a signal and returns the analog voltage level that would be created by a DAC if it were given the same number in binary.

    While value range is 0-1023, reference range is 0-5.00 volts. Value and reference is directly proportional.

    This DAC has 10 bits of resolution and the DAC reference is set at 5.00 volts.

Examples

    V_DAC(0) ➞ 0

    V_DAC(1023) ➞ 5

    V_DAC(400) ➞ 1.96

Notes

    You should return your value rounded to two decimal places.
    LINK: https://edabit.com/challenge/AJGqpNL2yAyhbdpvB

Thoughts

    take the input decimal value and convert proportionally using (n / 1023 * 5.00v), where n is the decimal input

    rounding to 2 decimal place will need to ceil or floor appropriately as opposed to truncating to two decimal places
"""

def V_DAC(value):
    output = round(((value / 1023) * 5.00), 2)
    return(output)

for i in range(1023):
    print(V_DAC(i))

# complete and tested July 9, 2023