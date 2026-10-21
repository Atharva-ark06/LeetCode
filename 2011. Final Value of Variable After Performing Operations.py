"""LeetCode 2011 — Final Value of Variable After Performing Operations.

Each operation either increments or decrements X by one.
Time: O(n); Space: O(1).
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for operation in operations:
            if "+" in operation:
                value += 1
            else:
                value -= 1
        return value


if __name__ == "__main__":
    solution = Solution()
    assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
    assert solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
    print("All sample tests passed.")
