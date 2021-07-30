# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	m = abs(n)
	for i in range(m):
		# print(n)
		if n < 0:
			s = s[-1] + s[:len(s)-1]
			
		elif n > 0:
			
			s = s[1:] + s[0]
			
		
	return s
print(fun_rotatestrings("abcd", -6))