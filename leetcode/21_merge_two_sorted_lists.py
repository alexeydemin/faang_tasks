from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


a4 = ListNode(4)
a2 = ListNode(2, a4)
a1 = ListNode(1, a2)

b4 = ListNode(4)
b3 = ListNode(3, b4)
b1 = ListNode(1, b3)

res = Solution.mergeTwoLists(None, list1=a1, list2=b1)

while res:
    print(res.val)
    res = res.next
