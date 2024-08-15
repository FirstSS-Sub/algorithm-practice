#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = []
        # d = {}
        # before_n = 1001
        # for i in range(len(numbers)):
        #     if numbers[i] != before_n:
        #         l.append(numbers[i])
        #         d[numbers[i]] = i
        #         before_n = numbers[i]
        #     else:
        #         if numbers[i]*2 == target: return [i, i+1]
        # for i in range(len(l)):
        #     for j in range(i+1, len(l)):
        #         if l[i] + l[j] == target:
        #             return [d[l[i]]+1, d[l[j]]+1]
        l, r = 0, len(numbers)-1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]

# @lc code=end
