class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        doub = 0
        miss = 0
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n in range(1, len(nums) + 1):
            if n not in freq:
                miss = n
            elif freq[n] == 2:
                doub = n
        res = [doub, miss]
        return res
            

 

                
        