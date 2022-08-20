class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans_count = 0
        if not s:
            return 0
        ans_count += dic[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if dic[s[i]] >= dic[s[i+1]]:
                ans_count += dic[s[i]]
            else:
                ans_count -= dic[s[i]]
        return ans_count
