class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def search(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break
                search(i, remaining - value, path + [value])
        search(0, target, [])
        return result
