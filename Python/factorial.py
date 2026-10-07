# Given a non-negative integer n, return the factorial of n.
# The factorial of a number n is the product of all positive integers from 1 to n.
# Formula: n! = n × (n-1) × ... × 1
# Note: 0! = 1.

def factorial(n: int) -> int:
    # Write your solution here
    fact=1
    if n>=0:
        for i in range (2, n+1):
            fact *= i
        return fact 