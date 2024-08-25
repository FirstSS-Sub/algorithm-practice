#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            idx = (l+r) // 2
            if nums[idx] == target: return idx
            elif nums[idx] < target:
                l = idx + 1
            else:
                r = idx
        return -1
        
# @lc code=end

