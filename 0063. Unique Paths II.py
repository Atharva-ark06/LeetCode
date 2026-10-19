class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        cols = len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1
        for row in obstacleGrid:
            for col, cell in enumerate(row):
                if cell == 1:
                    dp[col] = 0
                elif col:
                    dp[col] += dp[col - 1]
        return dp[-1]
