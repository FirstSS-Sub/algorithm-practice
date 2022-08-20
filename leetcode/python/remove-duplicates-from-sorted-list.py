# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        val_list = [head.val]
        tmp_val = head.val
        while head.next:
            hnv = head.next.val
            if tmp_val != hnv:
                val_list.append(hnv)
                tmp_val = hnv
            head = head.next
        val_list.sort(reverse=True)
        ans = ListNode(val_list[0], None)
        i = 1
        while i < len(val_list):
            tmp = ListNode(val_list[i], ans)
            ans = tmp
            i += 1
        return ans
        