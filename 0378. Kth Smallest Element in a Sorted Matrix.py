import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heap = [(matrix[row][0], row, 0) for row in range(min(rows, k))]
        heapq.heapify(heap)
        value = 0
        for _ in range(k):
            value, row, col = heapq.heappop(heap)
            if col + 1 < cols:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return value
