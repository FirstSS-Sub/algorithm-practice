#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root, l) -> list:
            if not root:
                l.append(None)
                return l
            l = dfs(root.left, l)
            l = dfs(root.right, l)
            l.append(root.val)
            return l
        return dfs(p, []) == dfs(q, [])
# @lc code=end

