"""LeetCode 1502 — Can Make Arithmetic Progression From Sequence.

Sort the values and check whether adjacent differences are equal.
Time: O(n log n); Space: O(n) for the sorted copy.
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ordered = sorted(arr)
        if len(ordered) < 3:
            return True
        difference = ordered[1] - ordered[0]
        return all(
            ordered[i] - ordered[i - 1] == difference
            for i in range(2, len(ordered))
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.canMakeArithmeticProgression([3, 5, 1]) is True
    assert solution.canMakeArithmeticProgression([1, 2, 4]) is False
    assert solution.canMakeArithmeticProgression([7]) is True
    print("All sample tests passed.")
