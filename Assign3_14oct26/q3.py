# Check if the Array is Sorted
# Given an array arr of size n, the task is to check if the given array is sorted in ascending (increasing or non-decreasing) order. If the array is sorted, return True; otherwise, return False.

# Examples:
# Example 1:
# Input:
# n = 5
# arr = [1, 2, 3, 4, 5]
# Output:
# True
# Explanation: The given array is sorted; every element in the array is smaller than or equals to its next value. Therefore, the answer is True.

# Example 2:
# Input:
# n = 5
# arr = [5, 4, 6, 7, 8]
# Output:
# False
# Explanation: The given array is not sorted; element 5 is not smaller than or equal to its next value 4. Therefore, the answer is False.

def isArraySorted(arr, n=None):
    
    if isinstance(arr, dict):
        arr = arr.get("arr", [])
        
    
    if n is None:
        n = len(arr)
        
    
    if n <= 1:
        return True
        
   
    for i in range(n - 1):
        if arr[i] is None or arr[i + 1] is None:
            return False
            
        if arr[i] > arr[i + 1]:
            return False
            
    return True
False
