#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        add_list(list1, l)
        add_list(list2, l)
        l.sort()
        if len(l) == 0: return None
        ans = ListNode()
        add_ans(ans, l, 0)
        return ans
            
        

def add_list(node: Optional[ListNode], l: List[int]):
    if node is not None:
        l.append(node.val)
        add_list(node.next, l)
        
def add_ans(ans: Optional[ListNode], l: List[int], i: int):
    ans.val = l[i]
    if i+1 == len(l): return
    ans.next = ListNode()
    add_ans(ans.next, l, i+1)

# @lc code=end

