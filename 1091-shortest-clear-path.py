''' https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid):

        # Can't ven start
        if grid[0][0] == 1:
            return -1

        # Stack for flood filling the maze
        flood_queue = [(0, 0)]
        # Since 1 is used for "obstacle", will count steps from 2
        grid[0][0] = 2


        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


        while flood_queue:
            x, y = flood_queue.pop()
            curr_step = grid[x][y]

            # Check 8 directions around the cell
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                # CHeck if it is not out of bounds
                if new_x < 0 or new_x == len(grid) or new_y < 0 or new_y == len(grid[0]):
                    continue

                # Ignore an obstacle
                if grid[new_x][new_y] == 1:
                    continue

                if grid[new_x][new_y] == curr_step:
                    pass

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
