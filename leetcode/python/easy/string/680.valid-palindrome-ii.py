#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        j = -1
        flag = True
        ans_flag = True
        for i in range((len(s)+1)//2):
            j += 1
            if s[i] == s[-(j+1)]: continue
            if not flag:
                ans_flag = False
                break
            j += 1
            if s[i] != s[-(j+1)]:
                ans_flag = False
                break
            flag = False
        if ans_flag: return True
        j = -1
        flag = True
        for i in range((len(s)+1)//2):
            j += 1
            if s[j] == s[-(i+1)]: continue
            if not flag:
                return False
            j += 1
            if s[j] != s[-(i+1)]:
                return False
            flag = False
        return True
            
        
# @lc code=end

