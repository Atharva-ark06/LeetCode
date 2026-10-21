"""LeetCode 1768 — Merge Strings Alternately.

Append paired characters, then append the remainder of the longer string.
Time: O(n + m); Space: O(n + m) for the result.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        limit = min(len(word1), len(word2))
        for i in range(limit):
            merged.extend((word1[i], word2[i]))
        merged.append(word1[limit:])
        merged.append(word2[limit:])
        return "".join(merged)


if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
    print("All sample tests passed.")
