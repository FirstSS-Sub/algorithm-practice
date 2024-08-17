#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] < height[r]:
                answer = max(answer, (r-l)*height[l])
                l += 1
            elif height[l] > height[r]:
                answer = max(answer, (r-l)*height[r])
                r -= 1
            else:
                answer = max(answer, (r-l)*height[l])
                l += 1
                r -= 1
        return answer
# @lc code=end
