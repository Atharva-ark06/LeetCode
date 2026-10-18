"""LeetCode 53: Maximum Subarray.

Kadane's algorithm tracks the best subarray ending at the current position.
Either extend the previous subarray or start a new one at the current value.

Time: O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = best = nums[0]

        for value in nums[1:]:
            current = max(value, current + value)
            best = max(best, current)

        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert solution.maxSubArray([-3, -2, -5]) == -2
    print("All LeetCode 53 examples passed.")
