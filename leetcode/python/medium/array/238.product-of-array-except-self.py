#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                if zero_count >= 2:
                    return [0]*len(nums)
                elif zero_count == 1:
                    continue
            else:
                prod *= n
        ans = []
        for n in nums:
            if zero_count == 1 and n == 0:
                ans.append(prod)
            elif zero_count == 1:
                ans.append(0)
            else:
                ans.append(prod // n)
        return ans
# @lc code=end

