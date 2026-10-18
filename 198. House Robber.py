"""LeetCode 198: House Robber.

At each house choose between skipping it or robbing it plus the best two-back total.
Time: O(n); Space: O(1).
"""


class Solution:
    def rob(self, nums):
        two_back = one_back = 0
        for amount in nums:
            two_back, one_back = one_back, max(one_back, two_back + amount)
        return one_back


if __name__ == "__main__":
    solver = Solution()
    assert solver.rob([1, 2, 3, 1]) == 4
    assert solver.rob([2, 7, 9, 3, 1]) == 12
    assert solver.rob([]) == 0
    print("All tests passed.")
