#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        answer = -1
        first = 0
        second = 0
        for i in range(len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                answer = i
            elif nums[i] > second:
                second = nums[i]
        return answer if first >= second*2 else -1
# @lc code=end

