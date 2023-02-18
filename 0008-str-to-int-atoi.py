''' https://leetcode.com/problems/string-to-integer-atoi/
'''

class Solution:
    def myAtoi(self, s):

        return 0

def main():
    ''' Test myAtoi
    '''
    solution = Solution()

    test_cases = [
        "42",
        "   -42",
        "4193 with words",
    ]
    for string in test_cases:
        print(string, solution.myAtoi(string))

if __name__ == "__main__":
    main()
