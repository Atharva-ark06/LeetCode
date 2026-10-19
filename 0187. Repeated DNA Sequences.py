class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            part = s[i:i + 10]
            if part in seen:
                repeated.add(part)
            seen.add(part)
        return list(repeated)
