# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

# def issorted(a):
# 	# your code goes here
# 	asc_list = sorted(a)
# 	des_list = asc_list[::-1]

# 	if a == asc_list or a == des_list:
# 		return True
# 	else:
# 		return False
	# pass

# import time
# start_time = time.time()

# # print(issorted([1,2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
# print(time.time()-start_time)

def issorted(a):
	if len(a) <= 1 :
		return True
	else:
		ascending = True
		descending = True
		previous = a[0]
		for item in a[1:]:
			if ascending and item < previous:
				ascending = False
			if descending and item > previous:
				descending = False
			if not ascending and not descending:
				return False
			previous = item
		return True

print(issorted([1,3,4,5]))