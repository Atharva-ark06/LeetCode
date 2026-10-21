"""LeetCode 2413 — Smallest Even Multiple.

An even input is its own smallest even multiple; otherwise double it.
Time: O(1); Space: O(1).
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else 2 * n


if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestEvenMultiple(5) == 10
    assert solution.smallestEvenMultiple(6) == 6
    assert solution.smallestEvenMultiple(1) == 2
    print("All sample tests passed.")
