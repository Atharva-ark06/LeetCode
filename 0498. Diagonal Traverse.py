class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        rows, cols = len(mat), len(mat[0])
        result = []
        for diagonal in range(rows + cols - 1):
            cells = []
            r = max(0, diagonal - cols + 1)
            c = min(diagonal, cols - 1)
            while r < rows and c >= 0:
                cells.append(mat[r][c])
                r += 1
                c -= 1
            result.extend(cells[::-1] if diagonal % 2 == 0 else cells)
        return result
