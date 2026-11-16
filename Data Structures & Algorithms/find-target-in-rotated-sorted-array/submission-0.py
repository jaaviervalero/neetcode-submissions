class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:         # right side sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid
            else:                           #left side sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid  
                else: 
                    l = mid + 1

        return l if target == nums[l] else -1
       