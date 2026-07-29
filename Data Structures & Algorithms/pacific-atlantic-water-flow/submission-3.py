
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def bfs(starts):
            queue = deque(starts)
            seen = set(starts)

            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    new_r = r + dr
                    new_c = c + dc

                    if not (0 <= new_r < rows and 0 <= new_c < cols):
                        continue
                    if (new_r, new_c) in seen:
                        continue
                    if heights[new_r][new_c] < heights[r][c]:
                        continue
                    seen.add((new_r, new_c))
                    queue.append((new_r, new_c))
            return seen
        pacific_starts = (
            [(0, c) for c in range(cols)] + 
            [(r, 0) for r in range(rows)]
        )

        atlantic_starts = (
            [(rows - 1, c) for c in range(cols)] +
            [(r, cols - 1) for r in range(rows)]
        ) 

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]
    


                
                
            
                
                

        
