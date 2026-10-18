"""LeetCode 409: Longest Palindrome.

Use all pairs of each character and optionally one odd leftover.
Time: O(n); Space: O(k) for distinct characters.
"""


from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        counts = Counter(s)
        length = sum((count // 2) * 2 for count in counts.values())
        if length < len(s):
            length += 1
        return length


if __name__ == "__main__":
    solver = Solution()
    assert solver.longestPalindrome("abccccdd") == 7
    assert solver.longestPalindrome("a") == 1
    assert solver.longestPalindrome("bb") == 2
    print("All tests passed.")
