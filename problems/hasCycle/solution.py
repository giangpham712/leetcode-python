from typing import Optional

from dataStructures.ListNode import ListNode


class Solution:
    def solve(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        p1 = head
        p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next

            if p1 is None or p2 is None or p2.next is None:
                return False
            else:
                p2 = p2.next

            if p1 == p2:
                return True
