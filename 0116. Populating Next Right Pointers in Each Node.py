class Solution:
    def connect(self, root):
        if not root:
            return None
        level = root
        while level.left:
            node = level
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            level = level.left
        return root
