''' https://leetcode.com/problems/min-cost-climbing-stairs/
'''

class Solution:
    def minCostClimbingStairs(self, cost):

        for pos in range(2, len(cost)):

            cost[pos] += min(cost[pos-1], cost[pos-2])

        return min(cost[-1], cost[-2])

def main():
    ''' Test minCostClimbingStairs
    '''
    solution = Solution()

    test_cases = [
        [10,15,20],
        [1,100,1,1,1,100,1,1,100,1],
        [1, 2],
    ]
    for cost in test_cases:
        result = solution.minCostClimbingStairs(cost)
        print(f"{cost}: {result}")

if __name__ == "__main__":
    main()
