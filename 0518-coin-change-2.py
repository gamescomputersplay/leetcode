''' https://leetcode.com/problems/coin-change-ii/
'''

class Solution:
    def change(self, amount, coins):

        def recursive_ways(remaining_amount, start_with_coin):

            # There is only one way to have 0: all 0 coins
            if remaining_amount == 0:
                return 1
            # Reached and of coins but still have money - no good
            if  start_with_coin == len(coins):
                return 0

            # Dynamic programming
            if (remaining_amount, start_with_coin) in cache:
                return cache[(remaining_amount, start_with_coin)]

            this_coin = coins[start_with_coin]

            # Can't have smaller amount with bigger last coin
            if start_with_coin == len(coins) - 1 and remaining_amount < this_coin:
                return 0

            ways = 0

            for this_coin_amount in range(remaining_amount // this_coin + 1):

                ways += recursive_ways(
                    remaining_amount - this_coin * this_coin_amount,
                    start_with_coin + 1)

            cache[(remaining_amount, start_with_coin)] = ways
            return ways

        # Cache for cash, haha
        cache = {}

        # I fell starting with big ones may be a faster way
        coins.sort(reverse=True)
        return recursive_ways(amount, 0)

def main():
    ''' Test change
    '''
    solution = Solution()

    test_cases = [
        (5, [1,2,5]),
        (3, [2]),
        (10, [10]),
        (1000, [100, 50, 20, 10, 5, 2, 1]),
        (0, [1,2,3,]),
        (0, [7]),
    ]
    for amount, coins in test_cases:
        result = solution.change(amount, coins)
        print(amount, coins, result)

if __name__ == "__main__":
    main()
