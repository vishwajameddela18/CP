# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.
import math
def largestperfectsquare(n):
	# your code goes here
	
	if math.sqrt(n) - (math.floor(math.sqrt(n))) == 0:
		return n
	else:
		n = math.ceil(math.sqrt(n))
		res = (n-1)**2
		return res
	# pass
print(largestperfectsquare(37))