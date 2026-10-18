"""LeetCode 118: Pascal's Triangle.

Build each row from adjacent values in the previous row.
Time: O(numRows^2); Space: O(numRows^2) for the result.
"""


class Solution:
    def generate(self, numRows):
        triangle = []
        for row_index in range(numRows):
            row = [1] * (row_index + 1)
            for col in range(1, row_index):
                row[col] = triangle[-1][col - 1] + triangle[-1][col]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    solver = Solution()
    assert solver.generate(1) == [[1]]
    assert solver.generate(5) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
    ]
    assert solver.generate(0) == []
    print("All tests passed.")
