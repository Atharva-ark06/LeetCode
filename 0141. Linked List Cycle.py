"""LeetCode 141: Linked List Cycle.

Floyd's tortoise-and-hare algorithm advances one pointer by one node and
another by two. If a cycle exists, they eventually meet.

Time: O(n)
Space: O(1)

LeetCode provides the ListNode definition and constructs the input list.
"""


class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False
