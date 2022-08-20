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
        
        val_list = []
        tmp_val = head.val
        flag = True
        while head.next:
            hnv = head.next.val
            if tmp_val != hnv and flag:
                val_list.append(tmp_val)
                flag = True
            elif tmp_val != hnv:
                flag = True
            else:
                flag = False
            tmp_val = hnv
            head = head.next
        if flag:
            val_list.append(head.val)
        val_list.sort(reverse=True)
        ans = None
        for i in range(len(val_list)):
            tmp = ListNode(val_list[i], ans)
            ans = tmp
        return ans
        