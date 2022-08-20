# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_list = []
        i = 0
        while head != None:
            ans_list.append(head)
            i += 1
            head = head.next
        return ans_list[int(i/2)]