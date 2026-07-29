
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        cols = len(heights[0])
        rows = len(heights)
        # first put in set to not duplicately add corners
        for c in range(cols):
            pacific.add((0, c))
            atlantic.add((rows - 1, c))
        for r in range(rows):
            pacific.add((r, 0))
            atlantic.add((r, cols - 1))
        pacific_queue = deque(pacific)
        atlantic_queue = deque(atlantic)
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def bfs(queue, seen):
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

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result


                
                
            
                
                

        
