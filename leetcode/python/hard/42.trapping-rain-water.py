#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_list = [0]
        max_left = 0
        max_right_list = [0]
        max_right = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            max_left_list.append(max_left)
            max_right = max(max_right, height[-(i+1)])
            max_right_list.append(max_right)
        answer = 0
        for i in range(len(height)):
            min_lr = min(max_left_list[i], max_right_list[-(i+1)])
            answer += max(min_lr-height[i], 0)
        return answer
        
# @lc code=end

