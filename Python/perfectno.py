# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

# Example 1:
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14 1, 2, 4, 7, and 14 are all divisors of 28.

# Example 2:
# Input: num = 7
# Output: false

def checkPerfectNumber(num: int) -> bool:
    fact = 0
    for i in range(1, num):
        if num%i== 0:
            fact += i
    if fact == num:
        return True
    else: 
        return False


    # def checkPerfectNumber(num: int) -> bool:
    # sum=1
    # if num<=1:
    #     for i in range(2, (num//2)+1):
    #         if(num%1==0):
    #             sum+=i
    #             if (i != num//i):
    #                 sum += num//i
    #                 return sum == num
    # return False
 