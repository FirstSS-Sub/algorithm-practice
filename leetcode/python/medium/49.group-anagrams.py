#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import defaultdict

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_d = defaultdict(list)
        for s in strs:
            ans_d[tuple(sorted(s))].append(s)
        return ans_d.values()
            
# @lc code=end

