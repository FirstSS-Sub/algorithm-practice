#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from collections import defaultdict

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            if d[n] > 0: return True
            d[n] += 1
        return False
# @lc code=end

