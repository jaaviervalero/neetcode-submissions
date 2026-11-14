class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        waterLevel = 0
        l = 0
        r = len(height) - 1
        water = 0
        while l < r:
            minHeight = min(height[l], height[r])
            waterLevel = max(waterLevel, minHeight)

            if height[l] < height[r]:
                water += max(waterLevel - height[l], 0)
                l += 1
            else:
                water += max(waterLevel - height[r], 0)
                r -= 1
        return water

        