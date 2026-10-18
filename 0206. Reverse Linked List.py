"""LeetCode 206: Reverse Linked List.

Reverse each link in place while keeping track of the previous node, current
node, and next node so the remainder of the list is not lost.

Time: O(n)
Space: O(1)

LeetCode provides the ListNode definition and constructs the input list.
"""


class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
