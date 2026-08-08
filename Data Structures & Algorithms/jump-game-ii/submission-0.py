class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        current_end = 0
        # i represents every index that is reachable and see how far next jump could extend
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # ur at end of cur window of furthest u can go with curr amt of jumps, so jump forward to furthest place possible in this window, which is furthest 
            if i == current_end:
                jumps += 1
                current_end = farthest
            
        return jumps

        