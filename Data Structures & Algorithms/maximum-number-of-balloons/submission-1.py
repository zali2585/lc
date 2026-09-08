class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tCounter = Counter(text)
        return min(
            tCounter['b'], 
            tCounter['a'],
            tCounter['l'] // 2,
            tCounter['o'] // 2,
            tCounter['n']
        )

