"""LeetCode 49: Group Anagrams.

A 26-letter frequency tuple is a stable key for lowercase English words.
Words with the same character counts are collected in the same group.

Time: O(n * k), where n is the number of strings and k their max length.
Space: O(n * k) for the grouping keys and output.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert {frozenset(group) for group in result} == {
        frozenset(["eat", "tea", "ate"]),
        frozenset(["tan", "nat"]),
        frozenset(["bat"]),
    }
    assert solution.groupAnagrams([""]) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]
    print("All LeetCode 49 examples passed.")
