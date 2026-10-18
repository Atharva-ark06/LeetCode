"""LeetCode 70: Climbing Stairs.

The number of ways follows the Fibonacci recurrence.
Time: O(n); Space: O(1).
"""


class Solution:
    def climbStairs(self, n):
        one_back, two_back = 1, 1
        for _ in range(n - 1):
            one_back, two_back = one_back + two_back, one_back
        return one_back


if __name__ == "__main__":
    solver = Solution()
    assert solver.climbStairs(1) == 1
    assert solver.climbStairs(2) == 2
    assert solver.climbStairs(5) == 8
    print("All tests passed.")
