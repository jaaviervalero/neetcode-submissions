class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        viewed = set()
        n_cons = 0
        max_cons = 0
        for n in nums:
            if n not in viewed:
                viewed.add(n)
        
        for n in viewed:
            if n - 1 not in viewed:
                n_cons = 1
                while n + 1 in viewed:
                    n_cons += 1
                    n += 1
                max_cons = max(max_cons, n_cons)
        return max_cons        

