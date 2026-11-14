class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = "".join(c for c in s.lower() if c.isalnum())
        r = len(cleared) -1

        for l in range(len(cleared) // 2):
            if cleared[l] != cleared[r]:
                return False
            r -= 1
        
        return True
        
