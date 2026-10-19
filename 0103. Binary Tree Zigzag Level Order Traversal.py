from collections import deque

class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        if not root:
            return []
        queue, result, reverse = deque([root]), [], False
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[::-1] if reverse else level)
            reverse = not reverse
        return result
