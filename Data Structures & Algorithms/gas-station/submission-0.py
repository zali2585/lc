class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # checks immediately if total cost outweighs total gas available
        # if so, no start point will change the fact u just dont have enough gas
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        # for every start point, u test if its a good starting point 
        # if cost > gas at i, its not a good start point and so u should start from i + 1 and try again with empty tank
        # if it is ok start point, continue on adding to tank
        # if tank ever goes negative, greedy principle is nullified bc u know by this point that theres enough gas for full trip (by initial check) so just start from where u can always be positive bc that will be the one guaranteed solution
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0
        return start


        