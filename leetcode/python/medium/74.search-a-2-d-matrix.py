#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        while l < r:
            idx = (l+r) // 2
            if matrix[idx][0] == target: return True
            elif matrix[idx][0] < target:
                l = idx + 1
            else:
                r = idx
        row_idx = l - 1
        l, r = 0, len(matrix[row_idx])
        while l < r:
            idx = (l+r) // 2
            if matrix[row_idx][idx] == target: return True
            elif matrix[row_idx][idx] < target:
                l = idx + 1
            else:
                r = idx
        return False
# @lc code=end

