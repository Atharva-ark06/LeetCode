"""LeetCode 543: Diameter of Binary Tree. Time O(n), space O(h)."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val, self.left, self.right = val, left, right

class Solution:
    def diameterOfBinaryTree(self, root):
        best = 0
        def height(node):
            nonlocal best
            if node is None: return 0
            left, right = height(node.left), height(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)
        height(root)
        return best

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert Solution().diameterOfBinaryTree(root) == 3
    assert Solution().diameterOfBinaryTree(TreeNode(1)) == 0
    print("All tests passed.")
