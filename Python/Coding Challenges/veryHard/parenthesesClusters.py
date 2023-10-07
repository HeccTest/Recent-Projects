"""
Project

    Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

Examples

    split("()()()") ➞ ["()", "()", "()"]

    split("((()))") ➞ ["((()))"]

    split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

    split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

Notes


    - All input strings will only contain parentheses.
    - Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.

    LINK: https://edabit.com/challenge/Fpymv2HieqEd7ptAq

Thoughts

    - iterate through string linearly, every open parenthesis will increment a counter, and close parenthesis will decrement.
    - when counter reaches 0, the substring that was just iterated through will be appended onto a list.
    - process repeats itself

"""

def split(txt):
	counter = 0
	currString = ""
	output = []
	for i in txt:
		if(i == "("):
			counter += 1
			currString += "("
		else:
			counter -= 1
			currString += ")"
			if(counter < 1):
				output.append(currString)
				currString = ""
	return(output)

print(split("((()))(())()()(()())"))

# completed and tested July 19, 2023