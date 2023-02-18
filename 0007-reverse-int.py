''' https://leetcode.com/problems/reverse-integer/
'''

class Solution:

    def reverse(self, x):
        ''' Let's try to do it without the string reversal
        '''
        # Keep track if the number was negative
        negative = True if x < 0 else False
        x = abs(x)

        rev_x = 0

        # This cycle will copy the number over digit by digit
        while x > 0:
            
            rev_x *= 10
            rev_x += x % 10
            x = x // 10

        # Put the sign back on 
        if negative:
            rev_x *= -1
        
        # Kinda weird to do this check in Python, but okay
        if  rev_x < - (2 ** 31) or rev_x > 2**31 - 1:
            return 0

        return rev_x


    def reverse_cheating(self, x):
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


def run_with_time(func):
    ''' Time function func
    '''

    start = time.time()
    for _ in range(1000000):
        func(2**29)
    print(f"Done in {time.time() - start}")


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

    run_with_time(solution.reverse)
    run_with_time(solution.reverse_cheating)

if __name__ == "__main__":
    import time
    main()
