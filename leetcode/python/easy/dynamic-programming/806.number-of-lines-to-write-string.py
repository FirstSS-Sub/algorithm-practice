#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        width = 100
        for c in s:
            if width - widths[ord(c) - ord('a')] < 0:
                line += 1
                width = 100
            width -= widths[ord(c) - ord('a')]
        return [line, 100 - width]
# @lc code=end

