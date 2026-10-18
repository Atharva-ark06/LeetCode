"""LeetCode 88: Merge Sorted Array.

Fill nums from the end so existing values are not overwritten too early.
Time: O(m + n); Space: O(1).
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j, write = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1


if __name__ == "__main__":
    solver = Solution()
    first = [1, 2, 3, 0, 0, 0]
    solver.merge(first, 3, [2, 5, 6], 3)
    assert first == [1, 2, 2, 3, 5, 6]
    first = [1]
    solver.merge(first, 1, [], 0)
    assert first == [1]
    print("All tests passed.")
