class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev, second = second, nxt
        first, second = head, prev
        while second:
            a, b = first.next, second.next
            first.next = second
            second.next = a
            first, second = a, b
