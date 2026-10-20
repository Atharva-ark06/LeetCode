class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []
        def backtrack(start: int, path: list[int]) -> None:
            if len(path) == k:
                results.append(path.copy())
                return
            needed = k - len(path)
            for value in range(start, n - needed + 2):
                path.append(value)
                backtrack(value + 1, path)
                path.pop()
        backtrack(1, [])
        return results
