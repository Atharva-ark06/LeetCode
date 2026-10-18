"""LeetCode 303: Range Sum Query - Immutable.

Prefix sums make each inclusive range query constant time.
Preprocessing: O(n) time and space; sumRange: O(1) time.
"""


class NumArray:
    def __init__(self, nums):
        self._prefix = [0]
        for value in nums:
            self._prefix.append(self._prefix[-1] + value)

    def sumRange(self, left, right):
        return self._prefix[right + 1] - self._prefix[left]


if __name__ == "__main__":
    values = NumArray([-2, 0, 3, -5, 2, -1])
    assert values.sumRange(0, 2) == 1
    assert values.sumRange(2, 5) == -1
    assert values.sumRange(0, 5) == -3
    print("All tests passed.")
