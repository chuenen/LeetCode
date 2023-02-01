class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        for i in range(len(str2) + 1):
            r_str = str2[:-i] if i else str2
            if not str2.replace(r_str, "") and not str1.replace(r_str, ""):
                return r_str
        return ""
