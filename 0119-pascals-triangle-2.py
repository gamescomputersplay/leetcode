''' https://leetcode.com/problems/pascals-triangle-ii/
'''

class Solution:
    def getRow(self, rowIndex):

        result = [1 for _ in range(rowIndex + 1)]

        return result

def main():
    ''' Test getRow
    '''
    solution = Solution()

    test_cases = [
        num for num in range(4)
    ]
    for numRows in test_cases:
        result = solution.getRow(numRows)
        print(f"{numRows}, {result}")

if __name__ == "__main__":
    main()
