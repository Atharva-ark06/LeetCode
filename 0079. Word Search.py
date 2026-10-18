class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False

        def search(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[index]:
                return False
            char = board[r][c]
            board[r][c] = "#"
            found = (search(r + 1, c, index + 1) or
                     search(r - 1, c, index + 1) or
                     search(r, c + 1, index + 1) or
                     search(r, c - 1, index + 1))
            board[r][c] = char
            return found

        return any(search(r, c, 0) for r in range(rows) for c in range(cols))
