class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) -1
        while l < r:
            lenght = min(heights[l], heights[r])
            width = r - l
            area = lenght * width
            maxA = max(maxA, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxA

        