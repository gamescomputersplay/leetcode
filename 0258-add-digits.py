''' https://leetcode.com/problems/add-digits/
'''

class Solution:

    def addDigits(self, num):

        the_sum = 0
        while num > 0:
            digit = num % 10
            num //= 10
            the_sum += digit

        while the_sum > 9:
            the_sum -= 9

        return the_sum

    def addDigits_prev(self, num):
        if num < 10:
            return num
        return self.addDigits(sum(int(c) for c in str(num)))

def test_timing(runs):
    start = time.time()
    solution = Solution()
    for _ in range(runs):
        solution.addDigits(123456789123456789)
    elapsed = time.time() - start
    print(elapsed)

def main():
    ''' Test addDigits
    '''
    solution = Solution()

    test_cases = [
        38,
        0,
        123456789,
        984787638763948,
        1,
    ]

    for num in test_cases:
        result = solution.addDigits(num)
        print(num, result)

if __name__ == "__main__":
    import time
    main()
    test_timing(100000)
