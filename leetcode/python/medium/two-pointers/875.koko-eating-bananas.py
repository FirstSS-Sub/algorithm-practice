#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
import math

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, 10**9
        ans = 10**9
        while min_k <= max_k:
            k = (min_k+max_k) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time > h:
                min_k = k + 1
            elif time <= h:
                ans = min(ans, k)
                max_k = k - 1
        return ans
# @lc code=end

