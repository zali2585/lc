class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
        return res
"""
Basic idea:
squaring numbers changes order bc negative nums become positive always, and become bigger maybe than they used to be
but the biggest nums squared will always cluster around edges (most negative or most positive)
so initialize l and r pointer to find biggest at moment and equate that to curr index (index decided by reverse loop over len nums so u dont have to reverse bc ur going from biggest to smallest num so if u do append u will have decreasing order but u need increasing)
"""

            