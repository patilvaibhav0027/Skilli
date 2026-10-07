# Even or Odd
# Given an integer n, determine whether the number is even or odd. Return "Even" if it is even, and "Odd" if it is odd.

# Example 1:
# Input: n = 4
# Output: "Even"
# Example 2:
# Input: n = 7
# Output: "Odd"
# Example 3:
# Input: n = 0
# # Output: "Even"

def checkEvenOdd(n: int) -> str:

    if n%2==0:
        return "Even"
    else:
        return "Odd"