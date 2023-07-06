''' https://leetcode.com/problems/gray-code/
'''

class Solution:
    def grayCode(self, n):

        # Recursion end
        if n==1:
            return [0, 1]

        # Forward
        half = self.grayCode(n - 1)
        # And backward with 1 in from
        first_digit = 2 ** (n-1) 
        second_half = [first_digit + x for x in half[::-1]]

        return half + second_half

def main():
    ''' Test grayCode
    '''
    solution = Solution()

    test_cases = [
       1,
       2,
       3,
       4

    ]
    for n in test_cases:
        result = solution.grayCode(n)
        print(f"{n}: {result}")

if __name__ == "__main__":
    main()
