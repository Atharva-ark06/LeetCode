class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        copies = {}
        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copies[node].next = copies.get(node.next)
            copies[node].random = copies.get(node.random)
            node = node.next
        return copies[head]
