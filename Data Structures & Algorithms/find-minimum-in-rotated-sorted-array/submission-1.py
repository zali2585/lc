class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # < stops when l and r are equal, so u stop on one single minimum values
        # <= means u are searching for a target val bc u still havent checked that last min val, u just assume its the min but when u need to actually access and check that last val that l and r centered on, u do <=
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]