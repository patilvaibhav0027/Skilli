# Reverse an Integer
# You are given an integer n. Your task is to return the integer formed by placing the digits of n in reverse order. 
# Note that the result should not have leading zeros.
# Examples
# Example 1:
# Input: n = 25
# Output: 52
# Explanation: The reverse of 25 is 52.
# Example 2:
# Input: n = 123
# Output: 321
# Explanation: The reverse of 123 is 321.
def reverseInteger(n):
    rev = 0

    while n != 0:
        digit = n % 10
        rev =rev * 10 + digit
        n = n//10

    return rev