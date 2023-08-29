''' https://leetcode.com/problems/pascals-triangle/
'''

class Solution:
    def generate(self, numRows):

        result = [[1]]

        while len(result) < numRows:

            result.append([1] + 
                          [result[-1][i] + result[-1][i+1]
                           for i in range(len(result)-1)]
                          + [1])

        return result

def main():
    ''' Test connect
    '''
    solution = Solution()

    test_cases = [
        num for num in range(1, 31)
    ]
    for numRows in test_cases:
        result = solution.generate(numRows)
        print(f"{numRows}, {result}")

if __name__ == "__main__":
    main()
