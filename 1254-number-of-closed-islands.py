''' https://leetcode.com/problems/number-of-closed-islands/
'''

class Solution:
    def closedIsland(self, grid):

        islands = set()
        good_island_count = 0

        # Size of teh whole map
        size_x = len(grid)
        size_y = len(grid[0])

        # Go through the islands
        for i in range(size_x):
            for j in range(size_y):

                # Ignore water
                if grid[i][j] == 1:
                    continue

                # Ignore islands we already found
                if (i, j) in islands:
                    continue

                # Found new land
                current_island = set()
                flood_fill = [(i,j)]
                is_bad = False
                while flood_fill:

                    current_cell = flood_fill.pop()
                    current_island.add(current_cell)
                    x, y = current_cell

                    # Non closed islands would touch the sides of the map
                    if x == 0 or y == 0 or x == size_x-1 or y == size_y-1:
                        is_bad = True
                    
                    # 4-directional flood fill
                    for dx, dy in ((-1, -0), (0, -1), (1, 0), (0, 1)):
                        new_x = x + dx
                        new_y = y + dy
                        # Adjacent cell is out of bounds
                        if new_x < 0 or new_x > size_x - 1 or new_y < 0 or new_y > size_y - 1:
                            continue
                        # Ignore water
                        if grid[new_x][new_y] == 1:
                            continue
                        # We already looked at this one
                        if (new_x, new_y) in current_island:
                            continue
                        flood_fill.append((new_x, new_y))

                # If we were never next to edge - its a desired, closed island
                if not is_bad:
                    good_island_count += 1

                # Keep track of all teh islands we had so far
                islands = islands.union(current_island)

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

    ]
    for grid in test_cases:
        print()
        result = solution.closedIsland(grid)
        print(grid, result)



if __name__ == "__main__":
    main()