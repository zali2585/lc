class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        nums.sort()

        for n in nums:
            index = abs(n) - 1

            if nums[index] < 0:
                dup = nums[index] * -1
            else:
                nums[index] *= -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                mis = i + 1
        return [dup, mis]
            

 

                
        