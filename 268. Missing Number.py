"""LeetCode 268: Missing Number.

The expected arithmetic-series sum minus the actual sum gives the missing value.
Time: O(n); Space: O(1).
"""


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    solver = Solution()
    assert solver.missingNumber([3, 0, 1]) == 2
    assert solver.missingNumber([0, 1]) == 2
    assert solver.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All tests passed.")
