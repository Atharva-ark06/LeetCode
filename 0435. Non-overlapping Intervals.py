class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda item: item[1])
        end, removed = float("-inf"), 0
        for start, finish in intervals:
            if start < end:
                removed += 1
            else:
                end = finish
        return removed
