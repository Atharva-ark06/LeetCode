"""LeetCode 876: Middle of the Linked List. Time O(n), space O(1)."""
class ListNode:
    def __init__(self, val=0, next=None): self.val, self.next = val, next

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

def make(values):
    dummy = tail = ListNode()
    for value in values: tail.next = ListNode(value); tail = tail.next
    return dummy.next

if __name__ == "__main__":
    s = Solution()
    assert s.middleNode(make([1,2,3,4,5])).val == 3
    assert s.middleNode(make([1,2,3,4,5,6])).val == 4
    print("All tests passed.")
