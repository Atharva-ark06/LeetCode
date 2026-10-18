"""LeetCode 283: Move Zeroes.

Approach: Copy non-zero values forward, then fill the remaining positions
with zeroes. This preserves the relative order of non-zero values.
Time: O(n) | Extra space: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1

        for index in range(write, len(nums)):
            nums[index] = 0


if __name__ == "__main__":
    values = [0, 1, 0, 3, 12]
    Solution().moveZeroes(values)
    assert values == [1, 3, 12, 0, 0]
