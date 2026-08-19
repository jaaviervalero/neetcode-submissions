class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = {}
        for i, n in enumerate(nums):
            if target - n in viewed:
                return [viewed[target-n], i]
            viewed[n] = i
        
        return None