#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import defaultdict

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in range(len(s)):
            ds[s[i]] += 1
            dt[t[i]] += 1
        return ds == dt
        
# @lc code=end

