class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        def backtrack(start, path):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return result
