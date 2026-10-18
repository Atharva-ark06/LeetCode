"""LeetCode 387: First Unique Character in a String.

Approach: Count each character, then scan again to find the first count of 1.
Time: O(n) | Extra space: O(1) for the fixed lowercase-English alphabet.
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for index, character in enumerate(s):
            if counts[character] == 1:
                return index
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("aabb") == -1
