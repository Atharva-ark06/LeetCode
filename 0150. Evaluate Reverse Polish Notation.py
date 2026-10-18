class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right, left = stack.pop(), stack.pop()
                if token == "+":
                    value = left + right
                elif token == "-":
                    value = left - right
                elif token == "*":
                    value = left * right
                else:
                    value = int(left / right)
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[-1]
