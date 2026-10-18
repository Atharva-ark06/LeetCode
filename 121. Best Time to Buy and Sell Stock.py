"""
LeetCode 121 — Best Time to Buy and Sell Stock

Approach: Track the lowest price seen so far. At each day, calculate
the profit from buying at that minimum and selling today; retain the
largest profit. A single left-to-right pass is sufficient.

Time: O(n).
Space: O(1).
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        best_profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            best_profit = max(best_profit, price - lowest_price)

        return best_profit


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([2, 4, 1]) == 2
    print("All sample tests passed.")
