from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        if head in self.map:
            return self.map[head]

        node = Node(head.val, None, None)
        self.map[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
