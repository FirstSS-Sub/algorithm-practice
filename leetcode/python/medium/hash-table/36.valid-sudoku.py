#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from collections import defaultdict

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row & col
        for i in range(9):
            d_row = defaultdict(int)
            d_col = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.':
                    if d_row[board[i][j]] != 0: return False
                    else: d_row[board[i][j]] += 1
                if board[j][i] != '.':
                    if d_col[board[j][i]] != 0: return False
                    else: d_col[board[j][i]] += 1
        # 3x3
        for ii in range(3):
            for jj in range(3):
                d = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        if board[ii*3+i][jj*3+j] == '.': continue
                        if d[board[ii*3+i][jj*3+j]] != 0: return False
                        else: d[board[ii*3+i][jj*3+j]] += 1
        return True
# @lc code=end

