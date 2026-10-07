# Swap Without Temporary Variable
# Given two integers a and b, swap their values without using a third temporary variable. Return the swapped values as a list [a, b] (where the first element is the original b and the second element is the original a).

# Example 1:
# Input: a = 5, b = 10
# Output: [10, 5]

# Example 2:
# Input: a = -3, b = 7
# Output: [7, -3] 



def swapNumbers(a: int, b: int) -> list[int]:
    a=a+b
    b=a-b
    a=a-b

    # print([a,b])

    return[a, b]
