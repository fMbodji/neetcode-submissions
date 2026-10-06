class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check for edge cases
        if t == "" or len(s) < len(t):
            return ""

        countT , window = {}, {}
        res = [-1, -1], 
        min_len = float("inf")
        l=0 

        # initialize the countT map
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need = len(countT)
        have = 0
        
        # loop thru s
        for r in range(len(s)):
            # update count of each char in
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # update have 
            if c in countT and window[c] == countT[c]:
                have += 1

            # check if a potential result has been found
            while have == need:
                current_len = r - l + 1
                # update res if a shorter substring has been found
                if current_len < min_len:
                    min_len = current_len
                    res = s[l:r+1]
                # start shrinking to minimize that len further
                # by popping from left of the window
                c = s[l]
                window[c] -= 1   # decrement its count
                # update have if we popped a needed character
                if c in countT and window[c] < countT[c]:
                    have -= 1
                # slide l pointer since s[l] has been popped
                l += 1

        if min_len != float("inf"):
            return res
        else:
            return ""

        