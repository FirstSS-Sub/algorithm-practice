#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from collections import defaultdict

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # hash
        # temp_dict = defaultdict(int)
        # ans_stack = []
        # for i in range(len(temperatures), 0, -1):
        #     min_idx = len(temperatures)+1
        #     for j in range(temperatures[i-1]+1, 101):
        #         if temp_dict[j] > 0:
        #             min_idx = min(min_idx, temp_dict[j])
        #     if min_idx == len(temperatures)+1:
        #         ans_stack.append(0)
        #     else:
        #         ans_stack.append(min_idx - i)
        #     temp_dict[temperatures[i-1]] = i
        # return reversed(ans_stack)
        
        # stack
        ans = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                ans[stack_idx] = i - stack_idx
            stack.append([t, i])
        return ans
# @lc code=end

