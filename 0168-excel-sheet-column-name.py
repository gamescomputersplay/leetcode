''' https://leetcode.com/problems/excel-sheet-column-title/
'''

class Solution:
    def convertToTitle(self, columnNumber):
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string = ""

        while columnNumber > 0:
            columnNumber -= 1
            character = columnNumber % 26
            string += mapping[character]
            columnNumber //= 26

        return string[::-1]

def main():
    ''' Test convertToTitle
    '''
    solution = Solution()

    test_cases = [
        1, #A
        2, #B
        26, #Z
        27, #AA
        28, #AB
        701, #ZY
        2**31 - 1,

    ]
    for columnNumber in test_cases:
        result = solution.convertToTitle(columnNumber)
        print(columnNumber, result)

if __name__ == "__main__":
    main()
