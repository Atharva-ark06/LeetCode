"""
LeetCode 1480 — Running Sum of 1d Array

Approach: Keep a cumulative total while traversing the array. Each
running-sum value is the sum of the current value and all earlier values.

Time: O(n).
Space: O(1) auxiliary space if modifying the output array in place.
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print("All sample tests passed.")
