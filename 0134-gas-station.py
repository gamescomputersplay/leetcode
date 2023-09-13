''' https://leetcode.com/problems/gas-station/
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):

        curr_gas = 0
        min_gas = float("inf")
        best_station = None

        for pos, (this_gas, this_cost) in enumerate(zip(gas, cost)):

            curr_gas = curr_gas - this_cost + this_gas
            if curr_gas <= min_gas:
                min_gas = curr_gas
                best_station = pos + 1

        if curr_gas < 0:
            return -1

        return best_station % len(gas)


def main():
    ''' Test canCompleteCircuit
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5], [3,4,5,1,2]),
        ([2,3,4], [3,4,3]),
        ([1,2,3,4], [1,2,3,4]),
        ([5,1,4,3,2], [2,4,1,3,5]),
        ([1],[10]),
    ]
    for gas, cost in test_cases:
        result = solution.canCompleteCircuit(gas, cost)
        print(gas, cost, result)


if __name__ == "__main__":
    main()