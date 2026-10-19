class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        value = sign * int(str(abs(x))[::-1])
        return value if -(2**31) <= value < 2**31 else 0
