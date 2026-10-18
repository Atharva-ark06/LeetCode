"""LeetCode 392: Is Subsequence.

Approach: Advance through s only when its current character matches the
current character in t. Matching all of s proves it is a subsequence.
Time: O(len(s) + len(t)) | Extra space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matched = 0
        for character in t:
            if matched < len(s) and s[matched] == character:
                matched += 1
        return matched == len(s)


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc") is True
    assert Solution().isSubsequence("axc", "ahbgdc") is False
