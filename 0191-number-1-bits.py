''' https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hammingWeight(self, n):

        bits = 0

        while n > 0:
            bits += n % 2
            n //= 2

        return bits


def main():
    ''' Test hammingWeight
    '''
    solution = Solution()

    test_cases = [

        0, 1, 10, 87623847

    ]
    for n in test_cases:
        result = solution.hammingWeight(n)
        print(n, result)

if __name__ == "__main__":
    main()
