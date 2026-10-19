class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        remainder, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while remainder >= divisor:
            value, multiple = divisor, 1
            while remainder >= (value << 1):
                value <<= 1
                multiple <<= 1
            remainder -= value
            quotient += multiple
        return sign * quotient
