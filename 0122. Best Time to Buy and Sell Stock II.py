"""LeetCode 122: Best Time to Buy and Sell Stock II.

Capture every positive day-to-day price increase.
Time: O(n); Space: O(1).
"""


class Solution:
    def maxProfit(self, prices):
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


if __name__ == "__main__":
    solver = Solution()
    assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solver.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solver.maxProfit([7, 6, 4, 3, 1]) == 0
    print("All tests passed.")
