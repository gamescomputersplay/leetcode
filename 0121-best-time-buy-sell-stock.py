''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices):
        ''' Return max possible profit
        '''
        max_profit = 0
        min_price_so_far = prices[0]

        for price in prices:

            # Calculate max possible profit
            max_profit = max(max_profit, price - min_price_so_far)

            # Keep track of min price so far
            min_price_so_far = min(min_price_so_far, price)

        return max_profit

def main():
    ''' Test maxProfit
    '''
    solution = Solution()

    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1], 0), 
        ([0, 100], 100),
    ]
    for array, answer in test_cases:
        result = solution.maxProfit(array)
        print(array, result, result == answer)

def timing_test():
    ''' Long random tests
    '''
    solution = Solution()
    for power in range(15, 22):
        size = 2** power
        array = [random.randint(0, 10000) for _ in range(size)]
        start = time.time()
        solution.maxProfit(array)
        elapsed = time.time() - start
        print(f"{power}, Size: {size}, Time: {elapsed}")


if __name__ == "__main__":
    import time
    import random
    #main()
    timing_test()
