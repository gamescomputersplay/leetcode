''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices):
        ''' Return max possible profit
        '''
        return 0

def main():
    ''' Test maxProfit
    '''
    solution = Solution()

    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,3,5,6], 7),
        ([1], 0), 
        ([0, 100], 100),
    ]
    for array, answer in test_cases:
        result = solution.maxProfit(array)
        print(array, result, result == answer)

if __name__ == "__main__":
    main()
