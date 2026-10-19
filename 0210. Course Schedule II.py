from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
