class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def build(current: str, opened: int, closed: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return
            if opened < n:
                build(current + "(", opened + 1, closed)
            if closed < opened:
                build(current + ")", opened, closed + 1)
        build("", 0, 0)
        return result
