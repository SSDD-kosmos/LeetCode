# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                max_profit += prices[i] - start
            start = prices[i]
        return max_profit
        

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
