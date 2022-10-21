class TicTacToe:

    def __init__(self, n: int):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[col][row] = player
        print(self.grid)
        return self.get_winner()

    def get_winner(self):
        diagonal_1 = []
        diagonal_2 = []
        for row in self.grid:
            if len(set(row)) == 1:
                return row[0]
        for i, row in enumerate(list(zip(*self.grid))):
            if len(set(row)) == 1:
                return row[0]
            for j in row:
                diagonal_1.append(self.grid[i][j])
                diagonal_2.append(self.grid[i][self.n - 1 - j])
        if len(set(diagonal_1)) == 1:
            return diagonal_1[0]
        if len(set(diagonal_2)) == 1:
            return diagonal_2[0]
        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
moves = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# moves = [[1, 1, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
for m in moves:
    print(obj.move(*m))
