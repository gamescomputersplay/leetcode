''' https://leetcode.com/problems/number-of-islands/
'''

class Solution:
    def numIslands(self, grid):

        def clear_island(x, y):
            ''' Flood fill island with 0s
            '''

            stack = [(x, y)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = '0'

                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_i, new_j = i + di, j + dj

                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                        if grid[new_i][new_j] == '1':
                            stack.append((new_i, new_j))

        island_count = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    island_count += 1
                    clear_island(i, j)

        return island_count

def main():
    ''' Test numIslands
    '''
    solution = Solution()

    test_cases = [

        [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]],

        [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

    ]
    for grid in test_cases:
        result = solution.numIslands(grid)
        print(grid, result)

if __name__ == "__main__":
    main()

        