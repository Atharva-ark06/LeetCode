class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            pieces, i = [], 0
            while i < len(result):
                j = i
                while j < len(result) and result[j] == result[i]:
                    j += 1
                pieces.append(str(j - i) + result[i])
                i = j
            result = "".join(pieces)
        return result
