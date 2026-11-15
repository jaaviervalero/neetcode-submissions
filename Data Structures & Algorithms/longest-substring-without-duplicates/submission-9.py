class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        viewed = set()
        l = 0
        maxLenght = 0
        for r in range(len(s)):
            while s[r] in viewed:
                viewed.discard(s[l])
                l += 1
            viewed.add(s[r])
            maxLenght = max(maxLenght, len(viewed))
        return maxLenght
