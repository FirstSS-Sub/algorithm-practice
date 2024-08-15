#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        if t == "": return False
        s_i = 0
        for c in t:
            if c == s[s_i]: s_i += 1
            if s_i == len(s): return True
        return False
        
# @lc code=end

