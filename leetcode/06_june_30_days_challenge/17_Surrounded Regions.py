from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m = len(board)
        n = len(board[0])
        true_zeros = [[0 for i in range(n)] for j in range(m)]

        def mark(i, j):
            if board[i][j] == 'O':
                true_zeros[i][j] = 1
                if i + 1 < m and not true_zeros[i + 1][j]:
                    mark(i + 1, j)
                if i and not true_zeros[i - 1][j]:
                    mark(i - 1, j)
                if j + 1 < n and not true_zeros[i][j + 1]:
                    mark(i, j + 1)
                if j and not true_zeros[i][j - 1]:
                    mark(i, j - 1)

        for i in range(1, m - 1):
            if board[i][0] == 'O':
                mark(i, 0)
            if board[i][n - 1] == 'O':
                mark(i, n - 1)
        for j in range(1, n - 1):
            if board[0][j] == 'O':
                mark(0, j)
            if board[m - 1][j] == 'O':
                mark(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not true_zeros[i][j]:
                    board[i][j] = 'X'

        return board


# print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
# print(Solution().solve(
#     [
#         ["X","O","X","O","X","O"],
#         ["O","X","O","X","O","X"],
#         ["X","O","X","O","X","O"],
#         ["O","X","O","X","O","X"]
#     ]))
print(Solution().solve(
    [
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"]
    ]))
a = 5
[["O", "X", "X", "O", "X"],
 ["X", "O", "O", "X", "O"],
 ["X", "O", "X", "O", "X"],
 ["O", "X", "O", "O", "O"],
 ["X", "X", "O", "X", "O"]]
