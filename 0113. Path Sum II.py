class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        result = []
        def visit(node, remaining, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining:
                result.append(path.copy())
            else:
                visit(node.left, remaining - node.val, path)
                visit(node.right, remaining - node.val, path)
            path.pop()
        visit(root, targetSum, [])
        return result
