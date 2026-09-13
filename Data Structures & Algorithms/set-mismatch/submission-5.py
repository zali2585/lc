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
"""
Basically, the logic in this question is to what you're doing is your mapping every number in numbs to the actual index it should be at like granted that everything was correct and so by doing that you you take the number that you're at and the index it should be if everything was like correct like numbs minus the number absolute value of that in case it's already negative minus one that's the index it should be at and then you will go and basically check is the number at that index already negative if it is, that means you've seen that number already this exact number cause only one number can map that specific index and then if it is negative, that's your duplicate if it's not negative, you make it negative so you mark a scene basically negative in this sense means you've seen it and then after you've done that for all the numbers there should be every number in there should be negative, except the one number you didn't see because that's the only number that can mark to the index of the positive number because it's like a very simple formula. It's like number minus one and then you do another four loop go through every single number that should be in i news so you do like four iron range of lane numbs if the number is positive at like whatever number that is you take that current index you're at because that index means that add that index you never saw the number that should've mapped to that index you take that index add one so that you offset the index like index by zero and then you return that as the missing number
"""
 

                
        