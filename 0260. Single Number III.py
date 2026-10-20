class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_all = 0
        for value in nums:
            xor_all ^= value
        distinguishing_bit = xor_all & -xor_all
        first = second = 0
        for value in nums:
            if value & distinguishing_bit:
                first ^= value
            else:
                second ^= value
        return [first, second]
