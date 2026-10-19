class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        digits = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + digits[i + j + 1]
                digits[i + j + 1] = product % 10
                digits[i + j] += product // 10
        return "".join(map(str, digits)).lstrip("0")
