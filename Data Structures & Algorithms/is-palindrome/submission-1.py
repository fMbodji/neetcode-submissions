class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()
        print(s)
        n = len(s)
        i, j = 0, n-1
        while i <= j:
            if s[i] != s[j]:
                print(f"{s[i]} is different from {s[j]}")
                return False
            i += 1
            j -= 1
        return True
        