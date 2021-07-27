"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search2(arr,low,high,x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search2(arr, low, mid - 1, x) 
        else:
            return binary_search2(arr, mid + 1, high, x) 
    else:
        return -1

def binary_search(input_array, value):
    arr = input_array
    low = 0
    high = len(input_array)+1
    x = value
    return binary_search2(arr,low,high,x)
