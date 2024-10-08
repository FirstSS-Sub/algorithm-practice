#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def exchange(root: Optional[TreeNode]):
            if not root:
                return
            root.left, root.right = root.right, root.left
            exchange(root.left)
            exchange(root.right)
        exchange(root)
        return root
        
# @lc code=end

