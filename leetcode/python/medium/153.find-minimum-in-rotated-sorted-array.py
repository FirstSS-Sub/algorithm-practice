#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]: return nums[0]
        while l < r:
            idx = (l + r) // 2
            if nums[idx] < nums[l] and nums[idx] < nums[r]:
                r = idx - 1
            elif nums[idx] > nums[l] and nums[idx] > nums[r]:
                l = idx + 1
            elif nums[idx] < nums[r]:
                r = idx
            elif nums[idx] > nums[l]:
                l = idx
        print(l, r)
        return nums[l]
# @lc code=end

