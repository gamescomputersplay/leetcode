''' https://leetcode.com/problems/pascals-triangle-ii/
'''

class Solution:
    def getRow(self, numRows):

        result = [[1]]

        while len(result) < numRows + 1:

            result.append([1] + 
                          [result[-1][i] + result[-1][i+1]
                           for i in range(len(result)-1)]
                          + [1])

        return result[-1]

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
