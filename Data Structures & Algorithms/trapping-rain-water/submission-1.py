class Solution:
    def trap(self, height: List[int]) -> int:
        waterLevel = 0
        l = 0
        r = len(height) - 1
        water = 0
        while l < r:
            minHeight = min(height[l], height[r])
            waterLevel = max(waterLevel, minHeight)

            if height[l] < height[r]:
                water += waterLevel - height[l]
                l += 1
            else:
                water += waterLevel - height[r]
                r -= 1
        return water

        