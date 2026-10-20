class Solution:
    def partition(self, head, x: int):
        before_head, after_head = ListNode(0), ListNode(0)
        before, after = before_head, after_head
        while head:
            next_node = head.next
            head.next = None
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = next_node
        before.next = after_head.next
        return before_head.next
