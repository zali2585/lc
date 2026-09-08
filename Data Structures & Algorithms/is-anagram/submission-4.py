class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC = Counter(s)
        tC = Counter(t)

        return sC == tC
        