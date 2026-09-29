class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxFreq = 0
        maxSub = 0
        # do this type of loop, not while r < len(s) bc automatically moves r whenever doing so would be valid instead of clunky mechanical
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])
            # when window becomes invalid, shrink l
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -=1
                l += 1
            # after l has shrinked to let window become valid, store as maxSubstring, or if never entered loop itll just store current window size
            maxSub = max(maxSub, r - l + 1)
        return maxSub


"""
l = 0 
maxFreq = freq of most occuring char
for every r in len(s):
    add r to hashmap
    calculate maxfreq of either current max or maybe new max of newly added char
        if window is invalid:
            shrink l
            (might artifically let a non safe window be safe, but itll be same size as an actually safe substring size bc outer loop only expanded by 1 so inner loop will shrink only logically once to make it back to previously valid window size to set up window size for next outer loop iteration adding new r)
        store curr window to maxSub if its larger than curr maxSub
"""





        