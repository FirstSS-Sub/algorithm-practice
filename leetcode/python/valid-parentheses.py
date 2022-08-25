from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack):
                    p = stack.pop()
                else:
                    return False
                if not (p == '(' and c == ')' or p == '{' and c == '}' or p == '[' and c == ']'):
                    return False
        return True if not len(stack) else False