class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def dfs(row, col):
            if not(0 <= row < rows and 0 <= col < cols):
                return 0 
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            area = 1
            area += (
                dfs(row + 1, col) + 
                dfs(row - 1, col) + 
                dfs(row, col + 1) +
                dfs(row, col - 1)
            )
            return area
        for r in range(rows):
            for c in range (cols):
                area = max(area, dfs(r, c))
        return area
        


