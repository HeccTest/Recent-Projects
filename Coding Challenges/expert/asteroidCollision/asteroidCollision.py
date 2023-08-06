"""
Project

    You are given a list asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Examples

    asteroid_collision([-2, -1, 1, 2]) ➞ [-2, -1, 1, 2]

    asteroid_collision([-2, 1, 1, -2]) ➞ [-2, -2]

    asteroid_collision([1, 1, -2, -2]) ➞ [-2, -2]

    asteroid_collision([10, 2, -5]) ➞ [10]

    asteroid_collision([8, -8]) ➞ []

Notes

    - BONUS: Use only one loop (either for or while).

    link: https://edabit.com/challenge/kPHmvQPLbdEKYeM9L

Thoughts

    - things that matter
        - order of appearance: positive asteroids check right, negative check left.
        - magnitude of asteroid (size)
        - direction of asteroid (positive or negative)
	- asteroids are either going to be greater than 0, or less than. Does not make sense for an asteroid to be of size 0 (non-existent). I can use this to determine direction
	- if a collision occurs. I should not increase index, but instead delete the smaller asteroid

"""

def asteroid_collision(asteroids):
	i = 0
	while(i < len(asteroids)):
		# print("ASTEROID LEN:", len(asteroids), "\tINDEX:", i, "\tASTEROID:", asteroids[i]) # TESTING
		if(asteroids[i] > 0): # current asteroid is going right, peek next element if possible
			if(i == len(asteroids) - 1): # looking at right-most asteroid
				i += 1
			else:
				if(asteroids[i + 1] < 0): # asteroid on the right is oncoming; collision imminent
					if(asteroids[i] > abs(asteroids[i + 1])): # current asteroid is larger; destroy next asteroid
						asteroids.pop(i + 1)
					elif(asteroids[i] < abs(asteroids[i + 1])): # current asteroid is smaller; destroy current asteroid
						asteroids.pop(i)
					else: # asteroids are equal; destroy both
						asteroids.pop(i)
						asteroids.pop(i)
				else: # next element is also going right. These two asteroids will never collide. Increment index
					i += 1
		elif(asteroids[i] < 0): # current asteroid is going left, peek previous element if possible
			if(i == 0): # peek not possible, already left-most asteroid. Since going left, will never collide
				i += 1
			else:
				if(asteroids[i - 1] > 0): # prev asteroid is going right; collision imminent
					if(abs(asteroids[i]) > asteroids[i - 1]): # current asteroid is larger; destroy previous asteroid
						asteroids.pop(i - 1)
					elif(abs(asteroids[i]) < asteroids[i - 1]): # current asteroid is smaller; destroy current asteroid
						asteroids.pop(i)
					else: # asteroids are equal value; destroy both. Readjust index
						i -= 1
						asteroids.pop(i)
						asteroids.pop(i)
					i -= 1
				else: # previous asteroid is going left. Will never collide with current asteroid.
					i += 1
	return(asteroids)

# complete and tested Aug. 5, 2023. See test_asteroidCollision.py for test cases