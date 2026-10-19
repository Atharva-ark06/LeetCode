class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def search(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                search(i + 1, remaining - candidates[i], path + [candidates[i]])
        search(0, target, [])
        return result
