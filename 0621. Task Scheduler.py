from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        maximum = max(counts.values())
        tied = sum(count == maximum for count in counts.values())
        frame = (maximum - 1) * (n + 1) + tied
        return max(len(tasks), frame)
