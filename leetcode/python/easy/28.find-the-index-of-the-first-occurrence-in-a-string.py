#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                haystack_copy = haystack + "-"*j
                if haystack_copy[i+j] != needle[j]: break
                if j == len(needle)-1: return i
        return -1
        
# @lc code=end