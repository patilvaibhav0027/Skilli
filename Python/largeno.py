# Largest of Three Numbers
# Given three integers a, b, and c, find and return the largest number among them using conditional statements without relying on the built-in max() function.

# Example 1:
# Input: a = 10, b = 25, c = 15
# Output: 25
# Example 2:
# Input: a = -5, b = -2, c = -10
# Output: -2

def largestOfThree(a: int, b: int, c: int) -> int:
    # Write your solution here
    if a>=b and a>=c:
        return a
    elif b>c:
        return b
    else:
        return c 