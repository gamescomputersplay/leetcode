''' https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n):

        ways = [1, 1]
        for step in range(n-1):
            ways.append(ways[-1] + ways[-2])

        return ways[-1]

def main(verbose=True):
    ''' Test climbStairs
    '''
    solution = Solution()

    test_cases = [
        1,
        2,
        3,
        4,
        5,
        10,
        20,
        45,
    ]

    for n in test_cases:
        result = solution.climbStairs(n)
        if verbose:
            print(f"{n}: {result}")

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