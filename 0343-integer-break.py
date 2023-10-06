''' https://leetcode.com/problems/integer-break/
'''

class Solution:

    def integerBreak(self, n):

        def integerBreak_rec(n):

            if n < 5:
                return n

            if n in cache:
                return cache[n]

            max_product = 1
            for first in range(2, n//2 + 1):
                max_product = max(max_product, first * integerBreak_rec(n - first))

            cache[n] = max_product
            return max_product

        exceptions = {2:1, 3:2}
        if n in exceptions:
            return exceptions[n]

        cache = {}
        return integerBreak_rec(n)

def main():
    ''' Test integerBreak
    '''
    solution = Solution()

    test_cases = [
        i for i in range(2, 101, 7)
    ]

    for n in test_cases:
        result = solution.integerBreak(n)
        print(n, result)

if __name__ == "__main__":
    main()
        