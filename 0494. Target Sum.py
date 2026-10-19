class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        ways = {0: 1}
        for value in nums:
            updated = {}
            for total, count in ways.items():
                updated[total + value] = updated.get(total + value, 0) + count
                updated[total - value] = updated.get(total - value, 0) + count
            ways = updated
        return ways.get(target, 0)
