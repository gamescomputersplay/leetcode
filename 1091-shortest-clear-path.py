''' https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        return 0

def main():
    ''' Test shortestPathBinaryMatrix
    '''
    solution = Solution()

    test_cases = [

        [[0,1],[1,0]],
        [[0,0,0],[1,1,0],[1,1,0]],
        [[1,0,0],[1,1,0],[1,1,0]],  

    ]
    for grid in test_cases:
        solution = Solution()
        result = solution.shortestPathBinaryMatrix(grid)
        print(grid, result)


if __name__ == "__main__":
    main()
