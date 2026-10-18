"""LeetCode 155: Min Stack.

Store each value with the minimum seen at that stack depth.
All operations: O(1) time; Space: O(n).
"""


class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        current_min = min(val, self._stack[-1][1]) if self._stack else val
        self._stack.append((val, current_min))

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1][0]

    def getMin(self):
        return self._stack[-1][1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
    print("All tests passed.")
