"""
LeetCode 20 — Valid Parentheses

Approach: Use a stack. Push each opening bracket. For every closing
bracket, the stack must contain its matching opener at the top.
At the end, the stack must be empty.

Time: O(n) — each character is processed once.
Space: O(n) — in the worst case, all characters are opening brackets.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching_open = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in matching_open:
                if not stack or stack.pop() != matching_open[char]:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([)]") is False
    assert solution.isValid("{[]}") is True
    print("All sample tests passed.")
