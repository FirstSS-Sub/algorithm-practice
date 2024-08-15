#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from collections import defaultdict

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        answer = 0
        for n in d:
            if (n - 1) not in d:
                length = 0
                while (n + length) in d:
                    length += 1
                answer = max(answer, length)
        return answer
# @lc code=end

