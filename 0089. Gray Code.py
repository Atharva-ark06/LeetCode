class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        for bit in range(n):
            result += [value | (1 << bit) for value in reversed(result)]
        return result
