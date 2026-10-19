class Solution:
    def isSymmetric(self, root) -> bool:
        def mirror(a, b):
            if not a or not b:
                return a is b
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
        return True if not root else mirror(root.left, root.right)
