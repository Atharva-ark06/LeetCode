"""LeetCode 26: Remove Duplicates from Sorted Array.

Approach: Keep a write pointer for the next unique value. Since the input
is sorted, each new value differs from the last value written.
Time: O(n) | Extra space: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    values = [1, 1, 2]
    count = Solution().removeDuplicates(values)
    assert count == 2
    assert values[:count] == [1, 2]
