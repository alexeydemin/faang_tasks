class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head

    def print(self, node):
        i = 0
        while node:
            print(node.val,)
            node = node.next
            i += 1


#root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
r = Solution.oddEvenList(None, root)
#print(r)
Solution.print(None, r)
# 12345
# 13524
