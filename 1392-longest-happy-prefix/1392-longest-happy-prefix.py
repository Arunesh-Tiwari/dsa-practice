class Solution:
    def longestPrefix(self, s: str) -> str:
        res=""
        for i in range(1,len(s)):
            if s[0:i]==s[len(s)-i:]:
                res=s[0:i]
        return res