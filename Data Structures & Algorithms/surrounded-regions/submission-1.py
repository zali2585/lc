class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def bfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != "O":
                return
            board[r][c] = "T"

            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc
                bfs(new_r, new_c)

        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        

        

        