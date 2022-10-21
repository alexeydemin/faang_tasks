from collections import defaultdict


class TicTacToe:
    def __init__(self, n: int):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diag = 0
        self.dia2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        pl = 1 if player == 1 else -1
        self.rows[row] += pl
        self.cols[col] += pl
        if row == col:
            self.diag += pl
        if row + col == self.n - 1:
            self.dia2 += pl

        if abs(self.rows[row]) == self.n:
            return 1 if self.rows[row] > 0 else 2
        if abs(self.cols[col]) == self.n:
            return 1 if self.cols[col] > 0 else 2
        if abs(self.diag) == self.n:
            return 1 if self.diag > 0 else 2
        if abs(self.dia2) == self.n:
            return 1 if self.dia2 > 0 else 2

        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
moves = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# moves = [[1, 1, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
for m in moves:
    print(obj.move(*m))
