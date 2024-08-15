#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        space_flag = False
        for c in s:
            if c == " ": space_flag = True
            else:
                if space_flag:
                    space_flag = False
                    answer = 1
                else:
                    answer += 1
        return answer
        
# @lc code=end

