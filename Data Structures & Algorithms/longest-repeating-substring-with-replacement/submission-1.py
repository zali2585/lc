class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        r = 0
        longest = 0
        mx = 0
        for r in range(len(s)):
            added = s[r]
            freq[added] = freq.get(added, 0) + 1
            mx = max(mx, freq[added])
            if (r - l + 1) - mx > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest
