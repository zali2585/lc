from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        INF = 2**31 - 1

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        # () means tuples, immutable (never change or edit) --> since coords stay same whole time use tuple, not list
        dirs = ((-1, 0 ), (1, 0), (0, 1), (0, -1))


        while queue:
            row, col = queue.popleft()

            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue 
                if grid[new_row][new_col] != INF:
                    continue 
                grid[new_row][new_col] = grid[row][col] + 1
                queue.append([new_row, new_col])

            
                
                

