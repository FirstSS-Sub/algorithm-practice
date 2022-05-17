class Solution:
    def romanToInt(self, s: str) -> int:
        s += "0"
        ans_count = 0
        for i in range(len(s) - 1):
            if s[i] == "I":
                if s[i + 1] == "V" or s[i + 1] == "X":
                    ans_count -= 1
                else:
                    ans_count += 1
            elif s[i] == "V":
                ans_count += 1
            elif s[i] == "X":
                if s[i + 1] == "L" or s[i + 1] == "C":
                    ans_count -= 10
                else:
                    ans_count += 10
            elif s[i] == "L":
                ans_count += 50
            elif s[i] == "C":
                if s[i + 1] == "D" or s[i + 1] == "M":
                    ans_count -= 100
                else:
                    ans_count += 100
            elif s[i] == "D":
                ans_count += 500
            elif s[i] == "M":
                ans_count += 1000
        return ans_count
