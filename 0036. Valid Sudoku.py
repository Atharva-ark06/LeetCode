"""LeetCode 36: Valid Sudoku.

Track digits already seen in each row, column, and 3x3 box.
Time: O(1) for the fixed 9x9 board; Space: O(1).
"""


class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r // 3) * 3 + c // 3
                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
        return True


if __name__ == "__main__":
    solver = Solution()
    valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solver.isValidSudoku(valid)
    invalid = [row[:] for row in valid]
    invalid[0][2] = "5"
    assert not solver.isValidSudoku(invalid)
    print("All tests passed.")
