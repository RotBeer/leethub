class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        profit = 0
        for p in prices:
            if p < min_p:
                min_p = p
            elif p - min_p > profit:
                profit = p - min_p
        return profit