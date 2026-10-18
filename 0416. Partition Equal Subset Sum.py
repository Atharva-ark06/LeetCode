class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable = {0}
        for num in nums:
            reachable |= {value + num for value in reachable if value + num <= target}
            if target in reachable:
                return True
        return target in reachable
