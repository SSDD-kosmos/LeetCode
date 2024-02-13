# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        temp = head

        while temp and temp.next:
            next_distinct = temp.next

            while next_distinct and temp.val == next_distinct.val:
                next_distinct = next_distinct.next

            temp.next = next_distinct
            temp = next_distinct

        return head

