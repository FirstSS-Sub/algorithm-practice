# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        now = head
        while now is not None:
            val_list.append(now.val)
            now = now.next
        return val_list == val_list[::-1]
