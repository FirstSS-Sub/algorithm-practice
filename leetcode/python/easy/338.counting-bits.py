#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans_l = []
        for nn in range(n+1):
            answer = 0
            for i in range(16, -1, -1):
                if nn < 2**i: continue
                answer += 1
                nn = nn % 2**i
            ans_l.append(answer)
        return ans_l
# @lc code=end

