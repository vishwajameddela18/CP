# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

# def handtodice(hand):
# 	# your code goes hereP
# 	hand = str(hand)
# 	# print(tuple(hand))
# 	return tuple(map(int, list(hand)))

def handtodice(hand):
	# your code goes hereP
	x = hand
	lis = []
	while(x >0):
		digit = x%10
		lis.append(digit)
		x = x//10
	lis = lis[::-1]
	return(tuple(lis))
	
# 	lis = []
# 	s = str(hand)
# 	# for i in range(len(s)):
# 	while(hand >0):
# 		lis.append(hand%10)
# 		hand = hand//10

# 	return tuple(lis[: :-1])




# print(handtodice(123))