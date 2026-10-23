"""
LeetCode #28 — Find the Index of the First Occurrence in a String
Difficulty: Easy
Pattern: String matching / Knuth-Morris-Pratt (KMP)

Return the first index where needle occurs in haystack, or -1 when absent.
KMP preprocesses the pattern so a mismatch does not restart the search from
the beginning.

Time: O(n + m), where n=len(haystack) and m=len(needle)
Extra space: O(m)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # lps[i] is the length of the longest proper prefix of needle[:i+1]
        # that is also a suffix of that substring.
        lps = [0] * len(needle)
        matched = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[matched]:
                matched += 1
                lps[i] = matched
                i += 1
            elif matched:
                matched = lps[matched - 1]
            else:
                i += 1

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("aaaaa", "bba") == -1
    assert solution.strStr("mississippi", "issip") == 4
    assert solution.strStr("abc", "") == 0
    print("LeetCode #28 checks passed.")
