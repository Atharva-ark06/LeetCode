"""LeetCode 3: Longest Substring Without Repeating Characters.

Keep a sliding window with unique characters. The last-seen index lets the
left boundary skip past a repeated character without rescanning the window.

Time: O(n)
Space: O(min(n, alphabet size))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    print("All LeetCode 3 examples passed.")
