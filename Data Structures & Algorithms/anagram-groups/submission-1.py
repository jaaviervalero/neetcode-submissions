class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            hint = ''.join(sorted(word))
            dict.setdefault(hint, []).append(word)
        
        return list(dict.values())