from collections import deque

class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        queue, result = deque([root]), []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == 0:
                    rightmost = node.val
            result.append(rightmost)
        return result
