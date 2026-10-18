"""LeetCode 202: Happy Number.

A set detects when the digit-square process enters a cycle.
Time: O(log n) per transformation; Space: O(log n) for seen states.
"""


class Solution:
    @staticmethod
    def _digit_square_sum(number):
        total = 0
        while number:
            number, digit = divmod(number, 10)
            total += digit * digit
        return total

    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self._digit_square_sum(n)
        return n == 1


if __name__ == "__main__":
    solver = Solution()
    assert solver.isHappy(19)
    assert not solver.isHappy(2)
    print("All tests passed.")
