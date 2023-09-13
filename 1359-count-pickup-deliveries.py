''' https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
'''

class Solution:
    def countOrders(self, n):
        # [1, 2, 3, ... n] + [1, 3, 5, ... 2n-1]
        multipliers = list(range(1, n + 1)) + list(range(1, n*2, 2))

        # Product of all that
        result = 1
        for multiplier in multipliers:
            result *= multiplier
            if result > 1_000_000_007:
                result %= 1_000_000_007

        return result

def main():
    ''' Test countNegatives
    '''
    solution = Solution()

    test_cases = [
        i for i in range(1, 5)       
    ]
    for n in test_cases:
        result = solution.countOrders(n)
        print(n, result)


if __name__ == "__main__":
    main()
