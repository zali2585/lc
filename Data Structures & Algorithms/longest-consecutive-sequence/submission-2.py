class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        # iterate through seen to remove redundant checks for duplicate values 
        for n in seen:
            if n - 1 not in seen:
                count = 0
                while n in seen:
                    count += 1
                    n += 1
                longest = max(count, longest)
        return longest 



        
            


