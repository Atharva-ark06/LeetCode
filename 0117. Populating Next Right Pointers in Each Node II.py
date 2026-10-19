class Solution:
    def connect(self, root):
        if not root:
            return None
        level_start = root
        while level_start:
            dummy = Node(0)
            tail = dummy
            node = level_start
            while node:
                for child in (node.left, node.right):
                    if child:
                        tail.next = child
                        tail = child
                node = node.next
            level_start = dummy.next
        return root
