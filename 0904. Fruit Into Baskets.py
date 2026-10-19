from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        counts = defaultdict(int)
        left = best = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
