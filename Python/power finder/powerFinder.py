# TASK: find the first power of 16 strictly greater than 16^4 (65536) that does not contain a 1, 2, 4 or, 8 when written in base 10 (decimal)
# Code will be evaluated based on performance and elegance. Failure due to integer overflow is not accepted. Choose any language.

# Author: Kai Lun He
# Date: August 30, 2022

lowestPower = 5 # the starting point of our search (16 ^ 5)

def invalidNumFound(n):
    # return false if 1, 2, 4, or 8 is found. Using a function, so restrictions can easily be changed
    currentNum = pow(16, n) # 16 ^ n
    strNum = str(currentNum) # casting to string to iterate through each digit

    for i in range(len(strNum)):
        # iterate through each digit as a str value, if an unwanted number is found return false.
        if(strNum[i] == '1' or strNum[i] == '2' or strNum[i] == '4' or strNum[i] == '8'):
            return(False)
    return(True) # no unwanted numbers were found (yay!)

while(True):
    if(invalidNumFound(lowestPower)): # if this is true, that means we have found a number that does not contain any invalid numbers
        print("Number found: 16 ^ " + str(lowestPower) + " = " + str(pow(16, lowestPower)))
        break # breaks out of the while loop, ending the code
    # print(lowestPower) # testing 
    lowestPower += 1

# I have tested to about 16 ^ 30000. At which point, I believe the task is no longer possible. There is no such number that exists (if there is however, I would love to know about it!)
# additionally, I have tested the code with less number restrictions (ie. does not contain 1 or 8. An answer was found, so code is working to an extent)