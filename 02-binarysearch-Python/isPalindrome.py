# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and 
# returns True if the given n is a palindrome and prime and False otherwise.
# 


def isPalindrome(n):

    lis = list(map(str, str(n)))
    # print(lis, lis[::-1])
    if lis == lis[::-1]:
        # print("True")
        return True

    return False

def isPrime(n):
    if n < 1:
        return False
    else:
        for i in range(2, n):
            # print("Yes")
            if n%i == 0:
                return False
    return True
def isPalindromicPrime(n):

    if isPalindrome(n):
        if isPrime(n):
            return True
    return False

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")