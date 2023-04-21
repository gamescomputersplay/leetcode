''' https://leetcode.com/problems/minimum-path-sum/
'''

class Solution:
    def minPathSum(self, grid):

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

def main():
    ''' Test minPathSum
    '''
    solution = Solution()

    test_cases = [
       [[1,3,1],[1,5,1],[4,2,1]],
       [[1,2,3],[4,5,6]],
    ]

    for grid in test_cases:
        result = solution.minPathSum(grid)
        print(grid, result)

if __name__ == "__main__":
    main()
