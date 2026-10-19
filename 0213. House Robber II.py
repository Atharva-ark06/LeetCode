class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear(values):
            prev2 = prev1 = 0
            for value in values:
                prev2, prev1 = prev1, max(prev1, prev2 + value)
            return prev1
        return max(linear(nums[:-1]), linear(nums[1:]))
