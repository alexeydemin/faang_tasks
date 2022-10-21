import abc
from abc import ABC, abstractmethod
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        pass


class Plus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class Minus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()


class Multiply(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class Divide(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


class Number(Node):
    def __init__(self, val):
        self.val = val

    def evaluate(self) -> int:
        return self.val


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operators = {'+': Plus, '-': Minus, '*': Multiply, '/': Divide}
        stack = []
        for token in postfix:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[token](left, right))
            else:
                stack.append(Number(int(token)))
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

postfix = ["3", "4", "+", "2", "*", "7", "/"]
obj = TreeBuilder()
expTree = obj.buildTree(postfix)
ans = expTree.evaluate()
print(ans)  # 2
