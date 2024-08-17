#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    # def __init__(self) -> None:
    #     self.str_stack = []
        
    # def generateParenthesis(self, n: int) -> List[str]:
    #     self.append_token("", 2*n)
    #     ans_stack = []
    #     for s in self.str_stack:
    #         tmp_stack = []
    #         for c in s:
    #             if c == "(":
    #                 tmp_stack.append(c)
    #             else:
    #                 if not tmp_stack:
    #                     tmp_stack.append(c)
    #                     break
    #                 else:
    #                     if tmp_stack.pop() == ")":
    #                         tmp_stack.append(c)
    #                         break
    #         if not tmp_stack:
    #             ans_stack.append(s)
    #     return ans_stack
        
    # def append_token(self, s: str, n: int) -> None:
    #     if n == 0:
    #         return self.str_stack.append(s)
    #     self.append_token(s+"(", n-1)
    #     self.append_token(s+")", n-1)
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        
        def backtrack(open_n, closed_n) -> None:
            if open_n == closed_n == n:
                ans.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n+1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n+1)
                stack.pop()
        
        backtrack(0, 0)
        return ans
        
# @lc code=end

