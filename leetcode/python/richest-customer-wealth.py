class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for x in accounts:
            sum_x = sum(x)
            if ans < sum_x: ans = sum_x
        return ans