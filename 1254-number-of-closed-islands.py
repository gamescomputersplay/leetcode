''' https://leetcode.com/problems/number-of-closed-islands/
'''

class Solution:
    def closedIsland(self, grid):

        # 0 - land
        # 1 - water
        # 2 - visited land

        good_island_count = 0

        # Size of teh whole map
        size_x = len(grid)
        size_y = len(grid[0])

        # Relative neighbors for flood fill 
        directions = ((-1, -0), (0, -1), (1, 0), (0, 1))

        # Go through the islands
        for i in range(1, size_x-1):
            for j in range(1, size_y-1):

                # Ignore water and visited land
                if grid[i][j] in (1, 2):
                    continue

                # Found new land
                flood_fill = [(i,j)]
                is_bad = False
                while flood_fill:

                    # Work through the list of cells to work through
                    current_cell = flood_fill.pop()  
                    x, y = current_cell

                    # Update grid as visited
                    grid[x][y] = 2

                    # If it touches the edge - it is not a "closed" island
                    if x == 0 or y == 0 or x == size_x-1 or y == size_y-1:
                        is_bad = True
                    
                    # 4-directional flood fill
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy

                        # Check if Adjacent cell is in bounds
                        if size_x - 1 >= new_x >= 0 and size_y - 1 >= new_y >= 0:

                            # Ignore water or visited
                            if grid[new_x][new_y] in (1, 2):
                                continue
                            # Add to the list of cells to go thorough
                            flood_fill.append((new_x, new_y))

                # If we were never next to edge - its a desired, closed island
                if not is_bad:
                    good_island_count += 1

        return good_island_count

    
def main():
    ''' Test closedIsland
    '''
    solution = Solution()

    test_cases = [
        [
         [1,1,1,1,1,1,1,0],
         [1,0,0,0,0,1,1,0],
         [1,0,1,0,1,1,1,0],
         [1,0,0,0,0,1,0,1],
         [1,1,1,1,1,1,1,0]],

        [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]],

        [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]],

        [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
         ],

        [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]],


    ]
    for grid in test_cases:
        print()
        result = solution.closedIsland(grid)
        print(grid, result)

def large_case(size=100):
    grid = []
    for i in range(size):
        grid.append([random.randint(0,1) for _ in range(size)])
    solution = Solution()
    start = time.time()
    result = solution.closedIsland(grid)
    #print(grid, result)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import random
    import time
    main()
    large_case(50)
    large_case(100)
    large_case(200)
