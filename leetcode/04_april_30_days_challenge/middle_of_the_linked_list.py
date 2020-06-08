# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    def middleNode(self):
        temp = self.head
        count = 0

        while self.head:

            # only update when count is odd
            if (count & 1):
                temp = temp.next
            self.head = self.head.next

            # increment count in each iteration
            count += 1
        return temp.val

