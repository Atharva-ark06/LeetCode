from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        allowed = set(bank)
        if startGene == endGene:
            return 0
        if endGene not in allowed:
            return -1
        queue = deque([(startGene, 0)])
        seen = {startGene}
        alphabet = "ACGT"
        while queue:
            gene, steps = queue.popleft()
            for i, original in enumerate(gene):
                for char in alphabet:
                    if char == original:
                        continue
                    candidate = gene[:i] + char + gene[i + 1:]
                    if candidate == endGene:
                        return steps + 1
                    if candidate in allowed and candidate not in seen:
                        seen.add(candidate)
                        queue.append((candidate, steps + 1))
        return -1
