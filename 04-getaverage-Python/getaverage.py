# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s): 
	lis = s.split(",")
	print(lis)
	sum = 0.0
	count = 0
	for i in range(len(lis)):
		if lis[i].isnumeric():
			sum+= int(lis[i])
			count+= 1
	if sum >0.0:

		return (sum/count)
	return sum

print(fun_getaverage("a,12,c,14,6,0"))
