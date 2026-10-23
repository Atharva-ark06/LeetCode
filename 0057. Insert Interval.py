"""
LeetCode #57 — Insert Interval
Difficulty: Medium
Pattern: Intervals / linear scan

Insert a new interval into a list of non-overlapping intervals sorted by start.
Merge every interval that overlaps the new interval.

Time: O(n)
Extra space: O(n) for the returned list
"""


class Solution:
    def insert(self, intervals, newInterval):
        result = []
        index = 0
        count = len(intervals)
        start, end = newInterval

        # Keep intervals that finish strictly before the new interval.
        while index < count and intervals[index][1] < start:
            result.append(intervals[index])
            index += 1

        # Merge all overlapping intervals. Touching endpoints overlap.
        while index < count and intervals[index][0] <= end:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1

        result.append([start, end])
        result.extend(intervals[index:])
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2], [3, 10], [12, 16]
    ]
    assert solution.insert([], [5, 7]) == [[5, 7]]
    assert solution.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert solution.insert([[1, 2], [5, 7]], [3, 4]) == [[1, 2], [3, 4], [5, 7]]
    print("LeetCode #57 checks passed.")
