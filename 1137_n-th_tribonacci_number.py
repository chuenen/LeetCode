class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0:0, 1:1, 2:1}
        for i in range(n+1):
            if i not in dp:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
