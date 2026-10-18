class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = max_frequency = answer = 0
        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_frequency = max(max_frequency, counts[char])
            while right - left + 1 - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer
