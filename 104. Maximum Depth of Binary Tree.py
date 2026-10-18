"""LeetCode 104: Maximum Depth of Binary Tree.

Depth is one plus the deeper child subtree.
Time: O(n); Space: O(h) recursion stack, where h is tree height.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    solver = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solver.maxDepth(root) == 3
    assert solver.maxDepth(None) == 0
    print("All tests passed.")
