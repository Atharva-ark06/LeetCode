"""LeetCode 2114 — Maximum Number of Words Found in Sentences.

Count whitespace-separated words in every sentence and take the maximum.
Time: O(total characters); Space: O(1) auxiliary space.
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)


if __name__ == "__main__":
    solution = Solution()
    assert solution.mostWordsFound([
        "alice and bob love leetcode", "i think so too",
        "this is great thanks very much"
    ]) == 6
    assert solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3
    print("All sample tests passed.")
