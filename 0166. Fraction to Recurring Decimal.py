class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        integer, remainder = divmod(numerator, denominator)
        result = sign + str(integer)
        if remainder == 0:
            return result
        result += "."
        seen = {}
        decimals = []
        while remainder and remainder not in seen:
            seen[remainder] = len(decimals)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            decimals.append(str(digit))
        if remainder:
            index = seen[remainder]
            decimals.insert(index, "(")
            decimals.append(")")
        return result + "".join(decimals)
