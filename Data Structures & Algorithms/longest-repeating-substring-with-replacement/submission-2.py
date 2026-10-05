class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        longest = 0
        counts = {}
        for r in range(n):
            # curr_window = s[l:r+1]
            counts[s[r]] = counts.get(s[r], 0) + 1 
            window_len = r-l + 1
            max_count = max(counts.values())
            # num_char_to_replace = window_len - max_count 
            while window_len - max_count  > k:
                counts[s[l]] -= 1   
                l += 1
                window_len = r-l + 1
                max_count = max(counts.values())
            longest = max(longest, window_len)
        return longest

        