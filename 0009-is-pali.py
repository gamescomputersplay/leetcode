''' https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x):

        # Negatives are not pali
        if x < 0:
            return False

        # Make a copy we can mutate
        original = x
        opposite = 0

        # Mathematically reverse the number
        while original > 0:

            opposite *= 10
            opposite += original % 10
            original //= 10

        return x == opposite

def main():
    ''' test reverse
    '''
    test_cases = [
        121,
        -121,
        10,
        8778,
        8776,
        0
    ]

    solution = Solution()
    for number in test_cases:
        print(number, solution.isPalindrome(number))


if __name__ == "__main__":
    main()
