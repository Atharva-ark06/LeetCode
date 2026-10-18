class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        unreachable = amount + 1
        dp = [0] + [unreachable] * amount
        for value in range(1, amount + 1):
            for coin in coins:
                if coin <= value:
                    dp[value] = min(dp[value], dp[value - coin] + 1)
        return dp[amount] if dp[amount] != unreachable else -1
