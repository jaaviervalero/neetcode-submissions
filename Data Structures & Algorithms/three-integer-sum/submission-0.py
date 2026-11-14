class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol: set(tuple(int, int, int)) = set()
        s_nums = sorted(nums)
        for i in range(len(s_nums)):
            l = 0
            r = len(nums) - 1
            while l < i and r > i:
                sum = s_nums[i] + s_nums[l] + s_nums[r]
                if sum == 0:
                    sol.add((s_nums[i], s_nums[l], s_nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return list(sol)
