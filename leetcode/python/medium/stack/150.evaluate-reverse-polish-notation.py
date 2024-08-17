#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for n in tokens:
            if n == "+" or n == "-" or n ==  "*" or n== "/":
                after = num_stack.pop()
                before = num_stack.pop()
                if n == "+":
                    num_stack.append(int(before + after))
                elif n == "-":
                    num_stack.append(int(before - after))
                elif n == "*":
                    num_stack.append(int(before * after))
                elif n == "/":
                    num_stack.append(int(before / after))
            else:
                num_stack.append(int(n))
        return num_stack.pop()
# @lc code=end

