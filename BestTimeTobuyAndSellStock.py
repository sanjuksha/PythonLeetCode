class Solution(object):
    def maxProfit(self, prices):
        l , r = 0, 1 #Left l = buy, Right r = sell
        maxP = 0 # Max

        while (r < len(prices)):
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1

        return maxP



if __name__ == '__main__' :
    print("LeetCode Problem 121: Best time to buy and sell ")
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print("Max profit: ",result)