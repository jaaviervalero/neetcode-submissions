class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxBenefit = 0
        for r in range(len(prices)):
            benefit = prices[r] - prices[l]
            if benefit > maxBenefit:
                maxBenefit = benefit
            if prices[r] < prices[l]:
                l = r

        
        return maxBenefit


        