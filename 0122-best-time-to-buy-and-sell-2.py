''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

class Solution:
    def maxProfit(self, prices):

        # Can't make money here
        if len(prices) == 1:
            return 0

        profit = 0
        bought_at = None

        # First one: buy if it is goin up
        if prices[1] > prices[0]:
            bought_at = prices[0]

        # Go through all items except the first and the last one
        for i in range(1, len(prices) - 1):

            a, b, c = prices[i-1], prices[i], prices[i+1]

            # If it is a peak: sell
            if bought_at is not None \
               and (a < b or b > c) \
               and a <= b >= c:
                profit += prices[i] - bought_at
                bought_at = None

            # if it is a trough: buy
            if bought_at is None \
               and (a > b or b < c) \
               and a >= b <= c:
                bought_at = prices[i]

        # Last one
        if bought_at is not None and prices[-1] > bought_at:
            profit += prices[-1] - bought_at

        return profit

def main():
    ''' Test maxProfit
    '''
    solution = Solution()

    test_cases = [
        [7,1,5,3,6,4], #7
        [7,1,1,5,5,3,6,4], #7
        [1,2,3,4,5], #4
        [7,6,4,3,1], # 0
        [2, 2, 2, 2],
        [2,2,2,2,1,1,1,3,3,3],
        [2,1,2,0,1], #2
    ]
    for prices in test_cases:
        result = solution.maxProfit(prices)
        print(prices, result)


if __name__ == "__main__":
    main()
