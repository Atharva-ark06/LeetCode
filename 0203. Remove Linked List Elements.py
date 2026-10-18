"""LeetCode 203: Remove Linked List Elements.

A sentinel node makes removal at the head identical to any other removal.
Time: O(n); Space: O(1).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        sentinel = ListNode(0, head)
        previous = sentinel
        while previous.next:
            if previous.next.val == val:
                previous.next = previous.next.next
            else:
                previous = previous.next
        return sentinel.next


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    solver = Solution()
    assert to_list(solver.removeElements(from_list([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(solver.removeElements(from_list([7, 7]), 7)) == []
    print("All tests passed.")
