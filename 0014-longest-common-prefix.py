''' https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs):

        common = ""

        min_len = min(len(string) for string in strs)

        for position, letter in enumerate(strs[0][:min_len]):

            for string_n in range(1, len(strs)):

                if strs[string_n][position] != letter:
                    return common

            common += letter

        return common

def main():
    ''' Test intToRoman
    '''
    solution = Solution()

    test_cases = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["a"],
        ["aaa", ""]
    ]
    for strs in test_cases:
        result = solution.longestCommonPrefix(strs)
        print(strs, result)

if __name__ == "__main__":
    main()

