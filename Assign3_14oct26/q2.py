# Count of Odd Numbers in Array
# Given an array of n elements, the task is to return the count of the number of odd numbers in the array.
# Examples
# Example 1:
# Input: n=5, array = [1,2,3,4,5]
# Output: 3
# Explanation: The three odd elements are (1, 3, 5).

# Example 2
# Input: n=6, array = [1,2,1,1,5,1]
# Output: 5
# Explanation: The five odd elements are one 5 and four 1's.

# Constraints
# 1 <= n <= 1000
# -1000 <= array[i] <= 1000
# Now Your Turn!
# Pick the correct output for the given input:

def countOddNumbers(n, array):
    # Write your code here
    count = 0
    for n in array :
        if n % 2 != 0:
            count += 1
    return count