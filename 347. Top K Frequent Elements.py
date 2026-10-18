"""LeetCode 347: Top K Frequent Elements.

Bucket values by frequency; scan buckets from highest to lowest.
Time: O(n); Space: O(n).
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        frequencies = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, frequency in frequencies.items():
            buckets[frequency].append(value)

        answer = []
        for frequency in range(len(buckets) - 1, 0, -1):
            answer.extend(buckets[frequency])
            if len(answer) >= k:
                return answer[:k]
        return answer


if __name__ == "__main__":
    solver = Solution()
    assert set(solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert solver.topKFrequent([1], 1) == [1]
    print("All tests passed.")
