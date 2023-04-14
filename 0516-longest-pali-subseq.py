''' https://leetcode.com/problems/longest-palindromic-subsequence/
'''

class Solution:
    def longestPalindromeSubseq(self, s):
        return 0

def main():
    ''' Test longestPalindromeSubseq
    '''
    solution = Solution()

    test_cases = [
        "bbbab",
        "cbbd",
        "abacabacabcccanncbbacaca",
    
    ]
    for string in test_cases:
        result = solution.longestPalindromeSubseq(string)
        print(string, result)

if __name__ == "__main__":
    main()
