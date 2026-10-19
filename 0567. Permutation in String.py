from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        if size > len(s2):
            return False
        target = Counter(s1)
        window = Counter(s2[:size])
        if window == target:
            return True
        for right in range(size, len(s2)):
            left_char = s2[right - size]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            window[s2[right]] += 1
            if window == target:
                return True
        return False
