from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(i, j, board):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = 'T'
                dfs(i - 1, j, board)
                dfs(i + 1, j, board)
                dfs(i, j - 1, board)
                dfs(i, j + 1, board)

        m = len(board)
        n = len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if i in [0, m - 1] or j in [0, n - 1] and board[i][j] == "O":
                    dfs(i, j, board)
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
Solution.solve(Solution, board)
print(board)
# [
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "O", "X", "X"]
# ]

board = [["X"]]
Solution.solve(Solution, board)
print(board)
# [["X"]]
