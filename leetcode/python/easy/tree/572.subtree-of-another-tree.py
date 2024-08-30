#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, l) -> list:
            if not root:
                l.append(None)
                return l
            l = dfs(root.left, l)
            l = dfs(root.right, l)
            l.append(root.val)
            return l
        r_l = dfs(root, [])
        sub_l = dfs(subRoot, [])
        for i in range(len(r_l)-len(sub_l)+1):
            if r_l[i:i+len(sub_l)] == sub_l:
                return True
        return False
# @lc code=end

