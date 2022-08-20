# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checked_node_list = []
        checked_val_list = []
        while head and head.next:
            checked_node_list.append(head)
            checked_val_list.append(head.val)
            head = head.next
            if head.val in checked_val_list:
                for node in checked_node_list:
                    if node == head:
                        return node
        return None