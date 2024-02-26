# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        counter = 0
        while l1 or l2 or counter:
            if l1:
                counter += l1.val
                l1 = l1.next
            if l2:
                counter += l2.val
                l2 = l2.next

            node.next = ListNode(counter % 10)
            counter //= 10

            node = node.next

        return head.next



