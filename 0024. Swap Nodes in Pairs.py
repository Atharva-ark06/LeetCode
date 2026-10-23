"""
LeetCode #24 — Swap Nodes in Pairs
Difficulty: Medium
Pattern: Linked list / pointer manipulation

Swap every adjacent pair of nodes and return the new head. Node values are
not changed; only the links are rewired.

Time: O(n)
Extra space: O(1)

LeetCode supplies the ListNode definition.
"""


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            # Rewire: previous -> second -> first -> next pair.
            first.next = second.next
            second.next = first
            previous.next = second

            previous = first

        return dummy.next


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def make_list(values):
        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next

    def values(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    solution = Solution()
    assert values(solution.swapPairs(make_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert values(solution.swapPairs(make_list([1]))) == [1]
    assert values(solution.swapPairs(make_list([]))) == []
    assert values(solution.swapPairs(make_list([1, 2, 3]))) == [2, 1, 3]
    print("LeetCode #24 checks passed.")
