class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        sufix = 1
        for i in nums:
            res.append(prefix)
            prefix *= i
        for i in range(len(nums)-1, -1, -1):
            res[i] *= sufix
            sufix *= nums[i]
        return res
