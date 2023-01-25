import math
class Solution:
    def climbStairs(self, n: int) -> int:
        quotient = n // 2
        count = 1 # count is at least 1, when all step is 1.
        if n > 1:
            for i in range(1, quotient+1):
                num_of_steps = i + n - (2 * i)
                count += math.comb(num_of_steps, i)
        return count
