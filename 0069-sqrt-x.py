''' https://leetcode.com/problems/sqrtx/
'''

class Solution:
    def mySqrt(self, x):
        left = 0
        right = x + 1
        while True:

            center = (left + right) // 2

            if center ** 2 == x or center ** 2 < x < (center + 1) ** 2:
                return center

            if center ** 2 > x:
                right = center
            else:
                left = center


def main(verbose=True):
    ''' Test mySqrt
    '''
    solution = Solution()

    test_cases = [
       0,
       1,
       2,
       3,
       4,
       8,
       999_999,
       1_000_000,
       2 ** 31 -1,
    ]

    for x in test_cases:
        result = solution.mySqrt(x)
        if verbose:
            print(f"{x}: {result}")

def test_timing(runs=100):
    solution = Solution()
    start = time.time()
    for _ in range(runs):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    test_timing()