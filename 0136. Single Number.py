"""LeetCode 136: Single Number.

Approach: XOR cancels pairs because x ^ x == 0 and x ^ 0 == x.
Time: O(n) | Extra space: O(1)
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        for value in nums:
            answer ^= value
        return answer


if __name__ == "__main__":
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
