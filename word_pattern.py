class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        data = s.split(' ')
        if len(set(pattern)) != len(set(data)) or len(pattern) != len(data):
            return False
        map = {}
        for p,d in zip(pattern, data):
            val = map.get(p)
            if not val:
                map[p] = d
                continue
            if val != d:
                return False
        return True
