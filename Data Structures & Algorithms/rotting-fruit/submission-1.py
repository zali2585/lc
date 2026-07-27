from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        minute = 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    new_r = r + dr
                    new_c = c + dc

                    if not (0 <= new_r < rows and 0 <= new_c < cols):
                        continue
                    if grid[new_r][new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c))
            minute += 1
        if fresh > 0:
            return -1
        return minute
                
            

