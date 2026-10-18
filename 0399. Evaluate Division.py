from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float],
                     queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        answers = []
        for start, target in queries:
            if start not in graph or target not in graph:
                answers.append(-1.0)
                continue
            queue = deque([(start, 1.0)])
            seen = {start}
            answer = -1.0
            while queue:
                node, product = queue.popleft()
                if node == target:
                    answer = product
                    break
                for neighbor, weight in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, product * weight))
            answers.append(answer)
        return answers
