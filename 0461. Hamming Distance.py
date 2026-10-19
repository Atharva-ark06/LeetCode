class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = x ^ y
        count = 0
        while value:
            value &= value - 1
            count += 1
        return count
