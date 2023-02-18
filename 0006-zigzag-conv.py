''' https://leetcode.com/problems/zigzag-conversion/
'''


class Solution:

    def convert(self, s, numRows):

        pass


def main():
    ''' test convert
    '''

    test_cases = [
        ("PAYPALISHIRING", 3), # PAHNAPLSIIGYIR
        ("PAYPALISHIRING", 4), # PINALSIGYAHRPI
        ("A", 1), # A
    ]

    solution = Solution()
    for string, num_rows in test_cases:
        print(string, num_rows, solution.convert(string, num_rows))

if __name__ == "__main__":
    main()
