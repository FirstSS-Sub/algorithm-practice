#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        cumulative_sum = [0]
        sum = 0
        for n in nums:
            sum += n
            cumulative_sum.append(sum)
        self.cumulative_sum = cumulative_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right+1]-self.cumulative_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
