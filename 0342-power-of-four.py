''' https://leetcode.com/problems/power-of-four/
'''

import math

class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        return int(math.log(n, 4)) == math.log(n, 4)


def main():
    ''' Test isPowerOfFour
    '''
    solution = Solution()

    test_cases = [
        16, 5, 1, 64, 256, 512, 1024, 128, -16, -1, -5, 0
    ]

    for n in test_cases:
        result = solution.isPowerOfFour(n)
        print(n, result)

if __name__ == "__main__":
    main()