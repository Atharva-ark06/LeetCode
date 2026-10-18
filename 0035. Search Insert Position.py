"""LeetCode 35: Search Insert Position.

Lower-bound binary search finds the first index whose value is >= target.
Time: O(log n); Space: O(1).
"""


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    solver = Solution()
    assert solver.searchInsert([1, 3, 5, 6], 5) == 2
    assert solver.searchInsert([1, 3, 5, 6], 2) == 1
    assert solver.searchInsert([1, 3, 5, 6], 7) == 4
    assert solver.searchInsert([], 4) == 0
    print("All tests passed.")
