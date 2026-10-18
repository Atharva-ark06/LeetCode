"""
LeetCode 238 — Product of Array Except Self

Approach: First store the product of all values to the left of each
position. Then sweep from right to left, multiplying each result by the
product of values to its right. No division is used.

Time: O(n).
Space: O(1) auxiliary space, excluding the required output array.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i, value in enumerate(nums):
            result[i] = prefix
            prefix *= value

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All sample tests passed.")
