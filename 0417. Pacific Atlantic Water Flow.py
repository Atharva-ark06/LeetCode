class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        def visit(starts, reachable):
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                if (r, c) in reachable:
                    continue
                reachable.add((r, c))
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (0 <= nr < rows and 0 <= nc < cols
                            and heights[nr][nc] >= heights[r][c]
                            and (nr, nc) not in reachable):
                        stack.append((nr, nc))
        visit([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)], pacific)
        visit([(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)], atlantic)
        return [[r, c] for r in range(rows) for c in range(cols)
                if (r, c) in pacific and (r, c) in atlantic]
