class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = "".join(c for c in s.lower() if c.isalnum())
        print(cleared)
        return cleared == cleared[::-1]
