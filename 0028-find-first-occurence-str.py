''' https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
'''

class Solution:
    def strStr(self, haystack, needle):
        return -1

def main():
    ''' test strStr
    '''
    test_cases = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
        ("helloworld", "low")
    ]

    solution = Solution()
    for haystack, needle in test_cases:
        print(haystack, needle, solution.strStr(haystack, needle))


if __name__ == "__main__":
    main()
