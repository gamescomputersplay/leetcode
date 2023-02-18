''' https://leetcode.com/problems/reverse-integer/
'''

class Solution:


    def reverse(self, x):
        ''' Works, but feels like cheating using string reversal
        '''

        negative = True if x < 0 else False

        x = abs(x)
        rev_x = int(str(x)[::-1])

        if negative:
            rev_x *= -1
        
        if  rev_x < - (2 ** 31) or rev_x > 2**31 - 1:
            return 0

        return rev_x


def main():
    ''' test reverse
    '''
    test_cases = [
        123,
        -123,
        120,
        987387676528325435243534523453453020746,
        2**29,
        2**31
    ]

    solution = Solution()
    for number in test_cases:
        print(number, solution.reverse(number))


if __name__ == "__main__":
    main()
