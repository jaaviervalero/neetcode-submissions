class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            lookingFor = target - n
            if lookingFor in seen:
                return [seen[lookingFor], i]
            seen[n] = i
        
        return None