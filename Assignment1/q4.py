# Palindrome Number
# You are given an integer n. Your task is to determine if n is a palindrome number.
# A palindrome number is one that reads the same when reversed.
# Examples:
# Example 1:
# Input: n = 121
# Output: true
# Explanation: When read from left to right: 121. When read from right to left: 121.
# Example 2:
# Input: n = 123
# Output: false
# Explanation: When read from left to right: 123. When read from right to left: 321.

def isPalindrome(n):
    rev = 0
    temp = n

    while n>0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n //10

    return temp == rev