''' https://leetcode.com/problems/factorial-trailing-zeroes/
'''

class Solution:
    def trailingZeroes(self, n):

        n_copy = n
        twos = 0
        while n_copy > 1:
            n_copy //= 2
            twos += n_copy

        n_copy = n
        fives = 0
        while n_copy > 1:
            n_copy //= 5
            fives += n_copy

        return min(twos, fives)

def main():
    ''' Test trailingZeroes
    '''
    solution = Solution()

    test_cases = [
        0, 3, 5, 
        10, 123, 5678,
    ]
    for n in test_cases:
        result = solution.trailingZeroes(n)
        print(n, result)

if __name__ == "__main__":
    main()
