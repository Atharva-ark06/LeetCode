from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        squares = [value * value for value in range(1, isqrt(n) + 1)]
        for value in range(1, n + 1):
            dp[value] = min(dp[value - square] + 1
                            for square in squares if square <= value)
        return dp[n]
