class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
