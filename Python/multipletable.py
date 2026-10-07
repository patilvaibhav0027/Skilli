# Multiplication Table
# Given an integer n and a positive integer limit, return a list containing the multiplication table of n from 1 up to limit (i.e. [n * 1, n * 2, ..., n * limit]).
# Example 1:
# Input: n = 3, limit = 5
# Output: [3, 6, 9, 12, 15]
# Example 2:
# Input: n = 7, limit = 3
# Output: [7, 14, 21]


def multiplicationTable(n: int, limit: int) -> list[int]:
    arr = []
    for i in range(1, limit+1):
        multiple=n*i
        arr.append(multiple)

    return arr     