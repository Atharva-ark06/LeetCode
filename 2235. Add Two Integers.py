"""LeetCode 2235 — Add Two Integers.

Return the sum of the two given integers.
Time: O(1); Space: O(1).
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


if __name__ == "__main__":
    solution = Solution()
    assert solution.sum(12, 5) == 17
    assert solution.sum(-10, 4) == -6
    assert solution.sum(0, 0) == 0
    print("All sample tests passed.")
