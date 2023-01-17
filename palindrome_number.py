class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        return val == val[::-1]
