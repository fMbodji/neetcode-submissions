class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        l=0
        max_length = 0
        char_dict = {}
        for r in range(n):
            if s[r] in char_dict and char_dict[s[r]] >= l:
                l = char_dict[s[r]] + 1
            char_dict[s[r]] = r
            curr_length = r-l + 1
            max_length = max(max_length, curr_length)
        return  max_length 
            
