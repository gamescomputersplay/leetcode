''' https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x):
        pass

def main():
    ''' test reverse
    '''
    test_cases = [
        121,
        -121,
        10,
        8778,
        8776,
    ]

    solution = Solution()
    for number in test_cases:
        print(number, solution.isPalindrome(number))


if __name__ == "__main__":
    main()
