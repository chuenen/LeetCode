class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            pair1, pair2 = words[i], words[i+1]
            for j in range(len(pair1)):
                if j >= len(words[i+1]):
                    return False
                if pair1[j] == pair2[j]: continue
                if order.index(pair1[j]) > order.index(pair2[j]):
                    return False
                break
        return True
