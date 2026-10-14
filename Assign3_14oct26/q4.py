# Reverse an Array In-Place
# Given an array arr of n elements, the task is to reverse the given array in-place. 
# The reversal should not create a new array; instead, it should modify the original array.

# Example 1:

# Input:

# {"n": 5, "arr": [1, 2, 3, 4, 5]}
# Output:

# [5, 4, 3, 2, 1]
# Explanation: The reverse of the array [1, 2, 3, 4, 5] is [5, 4, 3, 2, 1].

# Example 2:

# Input:

# {"n": 6, "arr": [1, 2, 1, 1, 5, 1]}
# Output:

# [1, 5, 1, 1, 2, 1]
# Explanation: The reverse of the array [1, 2, 1, 1, 5, 1] is [1, 5, 1, 1, 2, 1].

def reverseArray(arr):
    if isinstance(arr, dict):
        arr = arr.get("arr", [])
        
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr
