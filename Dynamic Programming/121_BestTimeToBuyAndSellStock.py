from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buyDay = prices[0]
        maxProfit = 0

        for price in prices:
            if price < buyDay:
                buyDay = price
            else:
                profit = price - buyDay
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit

solution = Solution()
solution.maxProfit([7, 1, 5, 3, 6, 2])
