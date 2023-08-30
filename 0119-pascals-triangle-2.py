''' https://leetcode.com/problems/pascals-triangle-ii/
'''

class Solution:
    def getRow(self, rowIndex):

        result = [1] + [0 for _ in range(rowIndex)]

        # Perform rowIndex steps to go from [1] the result line
        for i in range(rowIndex):

            # Sum current list with current list moved to the right 1 positions
            for j in range(i+1, 0, -1):
                result[j] += result[j - 1]

        return result

def main():
    ''' Test getRow
    '''
    solution = Solution()

    test_cases = [
        num for num in range(14)
    ]
    for numRows in test_cases:
        result = solution.getRow(numRows)
        print(f"{numRows}, {result}")

if __name__ == "__main__":
    main()
