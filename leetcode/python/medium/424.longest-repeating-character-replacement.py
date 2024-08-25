#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
# @lc code=end

