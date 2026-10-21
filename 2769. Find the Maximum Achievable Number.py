"""LeetCode 2769 — Find the Maximum Achievable Number.

Each of t moves can increase num by one while decreasing target by one,
so the maximum achievable target is num + 2*t.
Time: O(1); Space: O(1).
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == "__main__":
    solution = Solution()
    assert solution.theMaximumAchievableX(4, 1) == 6
    assert solution.theMaximumAchievableX(3, 2) == 7
    assert solution.theMaximumAchievableX(1, 0) == 1
    print("All sample tests passed.")
