''' https://leetcode.com/problems/plus-one/
'''

class Solution:
    def plusOne(self, digits):
        # This one feels like cheating

        string = "".join(str(n) for n in digits)
        num = int(string) + 1
        return [int(c) for c in str(num)]


    def plusOne_v2(self, digits):

        # List to number
        power = 10 ** (len(digits) - 1)
        num = 0
        for digit in digits:
            num += digit * power
            power //= 10
        
        # Plus one
        num += 1

        # Number to list
        
        new_length = len(digits)
        if digits.count(9) == len(digits):
            new_length += 1
        power = 10 ** (new_length - 1)

        new_digits = []
        for _ in range(new_length):
            new_digits.append(num // power)
            num %= power
            power //= 10

        return new_digits
    
    def plusOne_v1(self, digits):
        # It breaks the input list, but looks like it's okay.

        carry = 1

        for pos in range(len(digits)- 1, -1, -1):

            digits[pos] += carry
            carry = digits[pos]//10
            digits[pos] = digits[pos]%10

        if carry == 1:
            digits = [1] + digits

        return digits

def main(verbose=True):
    ''' Test plusOne
    '''
    solution = Solution()

    test_cases = [
       [1, 2, 3],
       [4, 3, 2, 1],
       [9],
       [9, 9, 9, 9]
    ]

    for digits in test_cases:
        result = solution.plusOne(digits)
        if verbose:
            print(f"{digits} {result}\n")

def test_timing(runs=100000):

    start = time.time()
    for _ in range(runs):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    test_timing()
