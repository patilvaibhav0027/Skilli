# Count of Prime Numbers till N
# You are given an integer . 
# Your task is to find out the number of prime numbers in the range [1, n] (inclusive).
#  A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.
# Example
# Example 1:
# Input: n = 6
# Output: 3
# Explanation: The prime numbers in the range [1, 6] are 2, 3, 5.
# Example 2:
# Input: n = 10
# Output: 4
# Explanation: The prime numbers in the range [1, 10] are 2, 3, 5, 7.
def countPrimes(n):
    count=0

    for num in range (2, n):
        divisor = 0
        for i in range (2, num):
            if num%i == 0:
                divisor += 1
        if divisor == 0:            
            count+=1
    return count