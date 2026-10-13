class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
      import heapq
      heap = [(grid[0][0], 0, 0)]
      seen = {(0,0)}
      n = len(grid[0])
      
      time = 0
      dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

      while heap:
        val, x, y = heapq.heappop(heap)
        time = max(time, val)
        if (x, y) == (n-1, n-1):
          return time

        for dx, dy in dirs:
          nx, ny = dx + x, dy + y
          if (0 <= nx < n) and (0 <= ny < n) and (nx, ny) not in seen:
            seen.add((nx, ny))
            heapq.heappush(heap, (grid[nx][ny], nx, ny))




        


      
"""
Input: grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]
]

Output: 8
"""
