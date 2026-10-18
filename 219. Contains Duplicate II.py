"""LeetCode 219: Contains Duplicate II.

Remember each value's latest index and check whether the distance is <= k.
Time: O(n); Space: O(n).
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}
        for index, value in enumerate(nums):
            if value in last_index and index - last_index[value] <= k:
                return True
            last_index[value] = index
        return False


if __name__ == "__main__":
    solver = Solution()
    assert solver.containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert solver.containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not solver.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print("All tests passed.")
