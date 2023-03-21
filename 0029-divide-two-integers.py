''' https://leetcode.com/problems/divide-two-integers/
'''
# In my understanding of the task division multiplication and mod operators
# are not allowed, but bit shift, comparison, addition and subtraction are.


class Solution:
    def divide(self, dividend, divisor):

        # Determine the sign of the result and "abs" the inputs
        negative = False
        for element in (dividend, divisor):
            if element < 0:
                negative = not negative

        dividend, divisor = abs(dividend), abs(divisor)

        # First let's find the maximum bit shift that will result in divisor > divident
        max_shift = 0
        power_2_value = 1
        while dividend > divisor:
            max_shift += 1
            power_2_value *= 2
            divisor *= 2

        # Now use subtraction to calculate quotient
        quotient = 0
        while max_shift >= 0:
            if divisor <= dividend:
                dividend -= divisor
                quotient += power_2_value

            max_shift -= 1
            divisor //= 2
            power_2_value //= 2

        # Abide by stupid 32 bit limitation
        if negative:
            answer = max(-(2**31), -quotient)
        else:
            answer = min(2**31-1, quotient)

        return answer


def main():
    ''' Test divide
    '''
    solution = Solution()

    test_cases = [
        [10, 3],
        [7, -3],
        [-10000, -123],
        [10, -1],
        [1, -10],
        [2**32, -1],
        [2**32, 1],

    ]
    for dividend, divisor in test_cases:
        quotient = solution.divide(dividend, divisor)
        print(f"{dividend} // {divisor} = {quotient}")


if __name__ == "__main__":
    main()