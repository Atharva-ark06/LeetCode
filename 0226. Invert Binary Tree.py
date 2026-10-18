"""LeetCode 226: Invert Binary Tree.

Swap left and right children recursively.
Time: O(n); Space: O(h) recursion stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    solver = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = solver.invertTree(root)
    assert result.left.val == 7 and result.right.val == 2
    assert result.left.left.val == 9 and result.right.right.val == 1
    assert solver.invertTree(None) is None
    print("All tests passed.")
