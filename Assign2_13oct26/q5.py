# Lowest Common Multiple (LCM) of Two Numbers
# You are given two integers n1 and n2. Your task is to find the Lowest Common Multiple (LCM) of the two given numbers. 
# The LCM of two integers is the smallest positive integer that is divisible by both integers.
# Examples
# Example 1:
# Input:
# n1 = 4, n2 = 6
# Output:
# 12
# Explanation:
# 4 * 3 = 12, 6 * 2 = 12.
# 12 is the lowest integer that is divisible by both 4 and 6.

# Example 2:
# Input:
# n1 = 3, n2 = 5
# Output:
# 15
# Explanation:
# 3 * 5 = 15, 5 * 3 = 15.
# 15 is the lowest integer that is divisible by both 3 and 5.


def findLcm(n1, n2):
    greater = 0
    if n1>n2:
        greater = n1
    else: 
        greater = n2
    while greater > 0:
        if greater % n1 == 0 and greater %n2 == 0:
            return greater
        greater += 1
    pass