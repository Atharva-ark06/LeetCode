class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        previous = [0] * (len(text2) + 1)
        for char1 in text1:
            current = [0]
            for j, char2 in enumerate(text2, start=1):
                if char1 == char2:
                    current.append(previous[j - 1] + 1)
                else:
                    current.append(max(previous[j], current[-1]))
            previous = current
        return previous[-1]
