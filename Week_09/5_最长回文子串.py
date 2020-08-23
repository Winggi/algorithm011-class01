class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == "": return ""
        elif len(s) == len(set(s)): return s[0]

        rev = s[::-1]
        ans = ''
        l = len(s)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if s[i:j+1] == rev[l-j-1:l-i] and j-i+1>len(ans):
                    ans = s[i:j+1]
                    
        if ans == '':return s[0]
        return ans