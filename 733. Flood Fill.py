"""LeetCode 733: Flood Fill. Time O(rows*cols), space O(rows*cols) worst case."""
class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]
        if original == color: return image
        rows, cols = len(image), len(image[0])
        def visit(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != original: return
            image[r][c] = color
            visit(r + 1, c); visit(r - 1, c); visit(r, c + 1); visit(r, c - 1)
        visit(sr, sc)
        return image

if __name__ == "__main__":
    s = Solution()
    assert s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert s.floodFill([[0,0],[0,0]], 0, 0, 0) == [[0,0],[0,0]]
    print("All tests passed.")
