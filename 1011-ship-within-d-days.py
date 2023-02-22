''' https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''

class Solution:
    def shipWithinDays(self, weights, days):
        
        return -1

def main():
    ''' Test shipWithinDays
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5), #15
        ([3,2,2,4,1,4], 3), #6
        ([1,2,3,1,1], 4), #3
    ]
    for weights, days in test_cases:
        result = solution.shipWithinDays(weights, days)
        print(weights, days, result)

if __name__ == "__main__":
    main()
