from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]):
        mx = 0
        fast = slow = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None

        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        while prev:
            mx = max(mx, prev.val + head.val)
            prev = prev.next
            head = head.next
        return mx


head1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print(Solution.pairSum(None, head1))  # 6

head2 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
print(Solution.pairSum(None, head2))  # 7
