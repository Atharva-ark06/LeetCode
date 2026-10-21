"""LeetCode 1672 — Richest Customer Wealth.

Sum each customer's accounts and return the largest total.
Time: O(m*n); Space: O(1) auxiliary space.
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert solution.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    print("All sample tests passed.")
