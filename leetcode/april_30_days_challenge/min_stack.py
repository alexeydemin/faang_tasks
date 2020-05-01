# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MinStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)

        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(x)

    def pop(self) -> None:
        node = self.head
        while node.next:
            if node.next.next is None:
                node.next = None
            else:
                node = node.next

    def top(self) -> int:
        node = self.head
        while node.next:
            node = node.next
        return node.data

    def getMin(self) -> int:
        node = self.head
        min = float("inf")
        while node:
            if node.data < min:
                min = node.data
            node = node.next
        return min


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
