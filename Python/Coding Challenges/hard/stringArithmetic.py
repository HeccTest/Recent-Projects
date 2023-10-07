"""
Project

    Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

    Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

    eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

Examples

    arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

    arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

    arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

    arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1

Notes

    All the inputs are only integers.

    The operators are * - + and //.

    Hint: Think about the single space that appears before and after the arithmetic operator.

    LINK: https://edabit.com/challenge/peezjw73G8BBGfHdW

Thoughts

    - input will be very strict. Probably just do a switch case, with string parsing
    - remember division by 0 should output -1 in this algorithm. Add an if statement, so I don't get a division by zero error.

"""
# n = "20 + 30"
def arithmetic_operation(n):
    inputVal = n.split(" ") # get a list of num1, operator, num2
    match(inputVal[1]):
        case "+":
            return(int(inputVal[0]) + int(inputVal[2]))
        case "-":
            return(int(inputVal[0]) - int(inputVal[2]))
        case "*":
            return(int(inputVal[0]) * int(inputVal[2]))
        case "//":
            if(inputVal[2] == "0"): # division by zero
                return(-1)
            else:
                return(int(inputVal[0]) / int(inputVal[2]))
            
# edabit is claiming line 39 has a syntax error. Maybe its using an older version of python and does not support match, case? Anyhow, will redo without using switch statements

def arithmetic_operation(n):
    inputVal = n.split(" ") # get a list of num1, operator, num2
    if(inputVal[1] == "+"):
        return(int(inputVal[0]) + int(inputVal[2]))
    elif(inputVal[1] == "-"):
        return(int(inputVal[0]) - int(inputVal[2]))
    elif(inputVal[1] == "*"):
        return(int(inputVal[0]) * int(inputVal[2]))
    elif(inputVal[1] == "//"):
        if(inputVal[2] == "0"): # division by zero
            return(-1)
        else:
            return(int(inputVal[0]) / int(inputVal[2]))

print(arithmetic_operation("12 + 12"))

print(arithmetic_operation("12 - 12"))

print(arithmetic_operation("12 * 12"))

print(arithmetic_operation("12 // 0"))

# complete and tested July 16, 2023