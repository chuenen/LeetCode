class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        for index, val in enumerate(s):
            if val == '(' and s[index+1] != ')' or val == '[' and s[index+1] != ']' or val == '{' and s[index+1] != '}':
                return False
        return True
        
