# Given a non-negative integer num, return the number of steps required to reduce it to 0. In each step:

# If num is even, divide it by 2.
# If num is odd, subtract 1 from it. Continue applying these operations until num becomes 0.
# Example
# For num = 14:
# 14 → 7 → 6 → 3 → 2 → 1 → 0 Total steps = 6. input:- 14
# output:- 6
# Output Return an integer representing the number of steps required to reduce num to 0. Constraints 0 <= num <= 10^9

def numberOfSteps(num: int) -> int:
    # Write your solution here
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps