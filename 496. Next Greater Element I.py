"""LeetCode 496: Next Greater Element I.

A monotonic decreasing stack resolves next-greater values in one pass.
Time: O(n + m); Space: O(n), where n = len(nums2), m = len(nums1).
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []
        for value in nums2:
            while stack and stack[-1] < value:
                next_greater[stack.pop()] = value
            stack.append(value)
        return [next_greater.get(value, -1) for value in nums1]


if __name__ == "__main__":
    solver = Solution()
    assert solver.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solver.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("All tests passed.")
