''' https://leetcode.com/problems/unique-paths-ii/
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

def main():
    ''' Test uniquePathsWithObstacles
    '''
    solution = Solution()

    test_cases = [
       [[0,0,0],[0,1,0],[0,0,0]],
       [[0,1],[0,0]],
       [[0,0,0,1,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0]],
    ]

    for obstacles in test_cases:
        result = solution.uniquePathsWithObstacles(obstacles)
        print(obstacles, result)

if __name__ == "__main__":
    main()
