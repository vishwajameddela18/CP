# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	lis = list(str(n))
	lis = lis[::-1]
	temp = "".join(lis)
	return int(temp)
# print(reverse(123))

def islychrel(n):
	print(n)
	for i in range(8):
		 
		m = reverse(n)
		if m == n or reverse(m+n) == m+n:
			return False
		n = m+n

	return True

def nthlychrelnumbers(n):
	# your code goes here
	k = 1
	count = n
	while(count > 0):

		if islychrel(k):
			count -= 1
		k += 1
	return k
	# pass

print(nthlychrelnumbers(1))