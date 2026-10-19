class Solution:
    def flatten(self, root) -> None:
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
