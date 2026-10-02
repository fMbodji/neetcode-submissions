class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        char_dict = {}
        for r in range(len(s)):
            if s[r] in char_dict and char_dict[s[r]] >= l:
                l = char_dict[s[r]] + 1
            char_dict[s[r]] = r
            res = max(res, r-l + 1)
        return res
            
