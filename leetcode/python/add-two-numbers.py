# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_val_list = []
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            ans_val_list.append(l1_val + l2_val)
        
        ans_num = 0
        for i in reversed(range(len(ans_val_list))):
            ans_num += ans_val_list[i] * (10 ** i)
        
        ans = None
        for value in [int(x) for x in list(str(ans_num))]:
            tmp = ListNode(value, ans)
            ans = tmp
        return ans