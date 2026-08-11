class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        # builds hashmap mapping char to last position it shows up
        for i, ch in enumerate(s):
            last[ch] = i
        res = []

        # end = last index substring must be to include all letter frequencies of letters included
        end = 0
        # start = where each partition start
        start = 0
        # you go through sequnce in one go
        for i in range(len(s)):
            ch = s[i]
            # u set end to whichever is larger, current needed end or the last pos of current char
            end = max(end, last[ch])
            # if even after changing end i == to it, then u reached end of sequence
            if i == end:
                # end - start + 1
                res.append(i - start + 1)
                start = i + 1
        return res
            
        