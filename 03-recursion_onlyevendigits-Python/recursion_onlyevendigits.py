# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def result_list(l, i):
    if len(l) == i:
        return l
    else:
        a = l[i]
        l[i] = reverse_digit(isdigit_even(a))
	
        return result_list(l, i + 1)
 
def isdigit_even(n, s=0):
    if n == 0:
        return s
    else:
        if (n % 10) % 2 == 0:
            return isdigit_even(n // 10, s=(s * 10) + (n % 10))
        else:
            return isdigit_even(n // 10, s)
 
def reverse_digit(n, s=0):
	
	if n == 0:
		return s
	else:

		rev = reverse_digit(n // 10, s=s * 10 + n % 10)
		return rev
 
def fun_recursion_onlyevendigits(l):
    if l == []:
        return []
    else:
        return result_list(l, 0)

