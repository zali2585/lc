class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        return len(string[-1])