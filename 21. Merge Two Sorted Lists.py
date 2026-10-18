"""LeetCode 21: Merge Two Sorted Lists.

Merge two sorted linked lists by reusing their nodes.
Time: O(m + n); Space: O(1) auxiliary (excluding the returned links).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    solver = Solution()
    assert to_list(solver.mergeTwoLists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(solver.mergeTwoLists(None, from_list([0]))) == [0]
    assert to_list(solver.mergeTwoLists(None, None)) == []
    print("All tests passed.")
