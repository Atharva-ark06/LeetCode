class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        import bisect
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
        if left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]
