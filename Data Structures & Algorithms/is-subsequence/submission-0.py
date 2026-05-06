class Solution:
    def isSubsequence(self, s: str, t: str):

        start = 0
        s_ch = 0
        while start < len(t) and s_ch < len(s):

           if t[start] == s[s_ch]:
               s_ch += 1
               start += 1
           else:
               start += 1
            
        if s_ch == len(s):
            return True
        else:
            return False
                