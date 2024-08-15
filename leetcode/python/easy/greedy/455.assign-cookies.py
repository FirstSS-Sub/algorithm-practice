#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        s_i = 0
        for gc in g:
            for _ in range(s_i, len(s)):
                if gc <= s[s_i]:
                    answer += 1
                    s_i += 1
                    break
                s_i += 1
        return answer

# @lc code=end
