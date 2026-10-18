from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for following in graph[course]:
                indegree[following] -= 1
                if indegree[following] == 0:
                    queue.append(following)
        return completed == numCourses
