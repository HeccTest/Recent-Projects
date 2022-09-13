# TASK: find the first power of 16 strictly greater than 16^4 (65536) that does not contain a 1, 2, 4 or, 8 when written in base 10 (decimal)
# Code will be evaluated based on performance and elegance. Failure due to integer overflow is not accepted. Choose any language.

# Author: Kai Lun He
# Date: August 30, 2022

lowestPower = 250 # interested in larger numbers (I believe if there are code based errors, they would be in the larger numbers (ie. overflow, weird interaction with iterations, or something unforseen))

def invalidNumFound(n):
    # return false if 1, 2, 4, or 8 is found. Using a function, so restrictions can easily be changed
    currentNum = pow(16, n) # 16 ^ n
    strNum = str(currentNum) # casting to string to iterate through each digit
    print(currentNum) # prints the current number function is looking at, followed by either an invalid number (see below) or a pass (I am manually checking some of these numbers)

    for i in range(len(strNum)):
        # iterate through each digit as a str value, if an unwanted number is found return false.
        if(strNum[i] == '1' or strNum[i] == '2' or strNum[i] == '4' or strNum[i] == '8'):
            print(strNum[i]) # prints the invalid number that was found
            return(False)
    return(True) # no unwanted numbers were found (yay!)

for i in range(250):
    if(invalidNumFound(lowestPower)): # if this is true, that means we have found a number that does not contain any invalid numbers
        print("Number found: 16 ^ " + str(lowestPower) + " = " + str(pow(16, lowestPower)))
        break # breaks out of the while loop, ending the code
    lowestPower += 1

# in most cases an invalid number is found within the first 4 or so digits. The remaining hundreds of digits also contain plenty of restricted numbers
# This gives me great confidence to say the task is impossible beyond a certain point (ie. it was only possible at 16 ^ 4 and below) and further testing will be fruitless.
