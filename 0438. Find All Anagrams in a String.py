from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        need = Counter(p)
        window = Counter(s[:len(p)])
        result = [0] if window == need else []
        for right in range(len(p), len(s)):
            left_char = s[right - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            window[s[right]] += 1
            if window == need:
                result.append(right - len(p) + 1)
        return result
