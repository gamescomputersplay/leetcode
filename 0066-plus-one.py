''' https://leetcode.com/problems/plus-one/
'''

# It breaks the input list, but looks like it's okay.

class Solution:
    def plusOne(self, digits):

        carry = 1

        for pos in range(len(digits)- 1, -1, -1):

            digits[pos] += carry
            carry = digits[pos]//10
            digits[pos] = digits[pos]%10

        if carry == 1:
            digits = [1] + digits

        return digits

def main():
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
        print(f"{digits} {result}\n")

if __name__ == "__main__":
    main()