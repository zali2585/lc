class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
      import heapq
      heap = []
      seen = {grid[0][0]}
      n = len(grid[0])
      x, y = 0, 0
      time = grid[0][0]
      dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

      while (x, y) != (n-1, n-1):
        for mx, my in dirs:
          nx = mx + x
          ny = my + y
          if (0 <= nx < n) and (0 <= ny < n):
            heapq.heappush(heap, (grid[nx][ny], (nx, ny)))
            # heap = [(2, (1, 0))]
        val, pos = heapq.heappop(heap)
        # val = 1
        while val in seen:
          val, pos = heapq.heappop(heap)
        x, y = pos[0], pos[1]
        # x, y = 0, 1
        time = max(time, grid[x][y])
        seen.add(val)
        # time = 1
      return time


        


      
"""
Input: grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]
]

Output: 8
"""
