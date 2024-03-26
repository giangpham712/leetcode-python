from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def solve(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copied = {}

        return self.__copy(head, copied)

    def __copy(self, node, copied):
        if node in copied:
            return copied[node]

        if node is None:
            return None

        copy = Node(node.val, None, None)
        copied[node] = copy
        if node.next is not None:
            copy.next = self.__copy(node.next, copied)

        if node.random is not None:
            copy.random = self.__copy(node.random, copied)

        return copy



