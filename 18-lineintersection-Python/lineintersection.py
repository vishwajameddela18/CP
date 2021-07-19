# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	
	if abs(m1) == abs(m2):
		return None
	else:

		x = (b2 - b1)/(m1 - m2)
		if x > 1.0:
			return abs(x)
		# if b1 == b2 and m1 == m2:
		# 	return x
	# a = m1*x + b1
	# b = m2*x + b2
	# # print(a, b)
	# if a == b:
	# 	# print(m1, b1, m2, b2, x)
	# 	return None

	# else:

		
