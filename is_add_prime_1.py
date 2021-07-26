# sAdditivePrime: Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.
# Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
# 29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.
# Here are sample test cases:



def isprime(n):
    if n<2:
        return False
    # elif n == 2 or n == 3:
    #     return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
            
    return True

def finddigitsum(n):
    lis = list(map(int, str(n)))
    sum = 0
    for i in range(len(lis)):
        sum+=lis[i]
    return sum

def isAdditivePrime(n):
    if isprime(n):
        if n < 9:
            return True
        else:
            sum = finddigitsum(n)
            if isprime(sum):
                return True
    return False

# print(isAdditivePrime(198))
assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")