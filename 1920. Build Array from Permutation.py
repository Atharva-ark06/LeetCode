"""LeetCode 1920 — Build Array from Permutation.

Use each permutation value as an index into nums.
Time: O(n); Space: O(n) for the output.
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[index] for index in nums]


if __name__ == "__main__":
    solution = Solution()
    assert solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
    print("All sample tests passed.")
