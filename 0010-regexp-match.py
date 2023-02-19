''' https://leetcode.com/problems/regular-expression-matching/
'''

class Solution:
    def isMatch(self, s, p):
        ''' Return whether string s is matching the regexp pattern p
        '''

def main():
    ''' test reverse
    '''
    test_cases = [
        ("aa", "a"), # False
        ("aa", "a*"), # True
        ("ab", ".*"), # True
        ("aabbccdee", "aa*cc.e"), # True
    ]

    solution = Solution()
    for string, pattern in test_cases:
        print(string, pattern, solution.isMatch(string, pattern))


if __name__ == "__main__":
    main()
