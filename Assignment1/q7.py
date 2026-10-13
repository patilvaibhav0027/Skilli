# Check if the Number is Armstrong
# You are given an integer n. You need to check whether it is an Armstrong number or not. 
# Return true if it is an Armstrong number, otherwise return false.
# An Armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
# Examples
# Example 1:
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

def isArmstrong(n):
    d = len(str(n))
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** d
        temp = temp // 10
    
    return total == n