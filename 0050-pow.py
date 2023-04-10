'''https://leetcode.com/problems/powx-n/
'''

class Solution:
    def myPow(self, x, n):

        result = 1

        is_reverse = False
        if n < 0:
            is_reverse = True
            n = abs(n)

        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            else:
                x *= x
                n //= 2

        if is_reverse:
            return 1 / result

        return result

def main():
    ''' Test myPow
    '''
    solution = Solution()

    test_cases = [
        (0, 1),
        (1, 0),
        (2, 10),
        (2.1, 3),
        (2, -2),
    ] + [(2, n) for n in range(1, 8)]
    for x, n in test_cases:
        result = solution.myPow(x, n)
        is_correct = result == x ** n
        print(x, n, result, is_correct)

if __name__ == "__main__":
    main()