''' https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


def main():
    ''' Test longestPalindrome
    '''
    solution = Solution()

    test_cases = [
        "babad", # "bab" or "aba"
        "cbbd", # bb
    ]
    for string  in test_cases:
        print(solution.longestPalindrome(string))

if __name__ == "__main__":
    main()
