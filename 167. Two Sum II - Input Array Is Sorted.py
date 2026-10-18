"""LeetCode 167: Two Sum II - Input Array Is Sorted.

Approach: Start at both ends. If the sum is too small, move the left pointer
up; if too large, move the right pointer down. Return 1-based indices.
Time: O(n) | Extra space: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
