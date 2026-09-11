class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = float('-inf')
        count = 0
        seen = set(nums)

        for n in nums:
            if n - 1 not in seen:
                while n in seen:
                    count += 1
                    n += 1
                longest = max(count, longest)
                count = 0
        return longest if longest != float('-inf') else 0



        
            


