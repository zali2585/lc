class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        tank = 0
        total = 0
        # for every point, u test if its a good addition to path, ie tank stays positive
        # if tank + gas[i] - cost[i] results in neg at i, its not a good start point and so u should start from i + 1 and try again with empty tank
        # if it is ok start point, continue on adding to tank
        # if tank ever goes negative, greedy principle is nullified bc u know by this point that theres enough gas for full trip (by initial check) so just start from where u can always be positive bc that will be the one guaranteed solution
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff

            if tank < 0:
                start = i + 1
                tank = 0
        # checks immediately if total cost outweighs total gas available
        # if so, no start point will change the fact u just dont have enough gas
        # at this point, total = all gas provided - all gas costed, meaning if its negative, there is just less gas available than gas needed to go around
        if total < 0:
            return -1 
        return start


        