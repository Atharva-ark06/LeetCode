"""
LeetCode #66 — Plus One
Difficulty: Easy
Pattern: Array / carry propagation

The digits array stores a non-negative integer from most significant to least
significant digit. Add one in place from right to left, carrying when a digit
becomes ten.

Time: O(n) worst case
Extra space: O(1) auxiliary space, excluding a possible leading digit
"""


class Solution:
    def plusOne(self, digits):
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            digits[index] = 0

        return [1] + digits


if __name__ == "__main__":
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert solution.plusOne([0]) == [1]
    print("LeetCode #66 checks passed.")
