"""
Project

    Write a function which takes an integer steps and returns a string representing an upward stair with steps representing the number of the steps in the stair. Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).

    So, if you print the result for a stair with three steps, it will look something like this:

      _
    _|
  _|
_|
    It's a crude and rickety stair, but challenging yourself in your favorite programming language is worth it.

Examples

    stair(1)  ➞ "  _\n_|"
    # 2 spaces, 1 underscore, 1 newline, 1 underscore, 1 vertical line

    stair(2)  ➞ "    _\n  _|\n_|"
    # 4 spaces, 1 undescore, 1 newline, 2 spaces, 1 underscore,
    # 1 vertical line, 1 newline, 1 underscore, 1 vertical line

    stair(3) ➞ "      _\n    _|\n  _|\n_|"
    # 6 spaces, 1 undescore, 1 newline, 4 spaces, 1 underscore,
    # 1 vertical line, 1 newline, 2 spaces, ...

    stair(4) ➞ "        _\n      _|\n    _|\n  _|\n_|"
    # 8 spaces, 1 undescore, 1 newline, 6 spaces, 1 underscore,
    # 1 vertical line,  ...

Notes


    - Since the stair is upward, the beginning of the code is the top of the stair.
    - All numbers are positive.
    - For zero, return ___ (three underscores).

    LINK: https://edabit.com/challenge/ZF9e922XuRaMu43Wp

Thoughts

    - valid output includes: " ", "\n", "_", "|"
    - if input = 0, output "___"
    - 2n spaces per layer
    - input is in range [0, inf)

"""

def stair(steps):
	if(steps == 0):
		return("___")
	else:
		output = (" " * 2 * steps) + "_\n"
		for i in reversed(range(steps)):
			output += ((" " * 2 * i) + "_|\n")
	output = output[:-1] # slice out the last item, an extra new line
	return(output)
	

print("  _\n_|")
print("    _\n  _|\n_|")
print("      _\n    _|\n  _|\n_|")
print(2*" ", "test")
print("--------------------------------------------------")

print(stair(0))
print(stair(1))
print(stair(2))
print(stair(3))
print(stair(4))
print(stair(5))

# completed and tested July 19, 2023