from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining = n
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)
