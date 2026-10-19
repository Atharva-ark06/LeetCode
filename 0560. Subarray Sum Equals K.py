from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        prefix = answer = 0
        for value in nums:
            prefix += value
            answer += prefix_counts[prefix - k]
            prefix_counts[prefix] += 1
        return answer
