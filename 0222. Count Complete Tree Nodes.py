class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        left_h, right_h = height(root.left), height(root.right)
        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        return (1 << right_h) + self.countNodes(root.left)
