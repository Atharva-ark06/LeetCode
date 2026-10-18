class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        positions = {value: i for i, value in enumerate(inorder)}
        self.index = 0

        def build(left: int, right: int):
            if left >= right:
                return None
            value = preorder[self.index]
            self.index += 1
            node = TreeNode(value)
            pivot = positions[value]
            node.left = build(left, pivot)
            node.right = build(pivot + 1, right)
            return node

        return build(0, len(inorder))
