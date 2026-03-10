# Leetcode Link: https://leetcode.com/problems/design-tic-tac-toe/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a Tic-Tac-Toe game on n x n board. move(row, col, player) returns winner (1 or 2) or 0.
# ---------- Approach ----------
# Track row/col/diagonal sums. Player 1 adds +1, player 2 adds -1.
# If any sum reaches +n or -n, that player wins. No need to store the full board!
# Time: O(1) per move | Space: O(n)
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        self.rows[row] += val
        self.cols[col] += val
        if row == col: self.diag += val
        if row + col == self.n - 1: self.anti_diag += val
        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or
                abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
            return player
        return 0
