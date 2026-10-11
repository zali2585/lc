class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_cost = [float('inf')] * len(points)
        next_point = 0
        min_weight = float('inf')
        total = 0
        visited.add(0)
        while len(visited) < len(points):
            x, y = points[next_point]
            for i, weight in enumerate(min_cost):
                if i in visited:
                    continue
                if i == next_point:
                    continue

                dist = abs(x - points[i][0]) + abs(y - points[i][1])
                min_cost[i] = min(min_cost[i], dist)
                if min_cost[i] < min_weight:
                    min_weight = min_cost[i]
                    next_point = i
            total += min_weight
            visited.add(next_point)
            min_weight = float('inf')
        return total





        