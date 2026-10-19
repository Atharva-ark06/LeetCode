class Solution:
    def rob(self, root) -> int:
        def visit(node):
            if not node:
                return 0, 0
            left_rob, left_skip = visit(node.left)
            right_rob, right_skip = visit(node.right)
            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_rob, left_skip) + max(right_rob, right_skip)
            return rob_node, skip_node
        return max(visit(root))
