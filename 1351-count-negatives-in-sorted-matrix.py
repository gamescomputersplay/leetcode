''' https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
'''

class Solution:
    def countNegatives(self, grid):

        # Overall size fo the matrix
        cols = len(grid[0])

        negative_count = 0

        # This pointer we want tp point
        # to the first negative number in the row
        # None is we don't know
        first_neg = None
        for row in grid:

            if first_neg is not None:

                # Move poinger to the left to the first negative number
                while row[first_neg-1] < 0 < first_neg:
                    first_neg -= 1

                negative_count += cols - first_neg

            # First time, or haven't found any negatived yet
            else:

                # This row does not have negatives, skip to teh next row
                if row[-1] >= 0:
                    continue

                # Look for the first negative
                for i in range(cols - 1, -1, -1):

                    if row[i] >= 0:
                        first_neg = i + 1
                        negative_count += cols - first_neg
                        break
                # The whole line must be negatives
                else:
                    first_neg = 0
                    negative_count += cols - first_neg

        return negative_count

def main():
    ''' Test countNegatives
    '''
    solution = Solution()

    test_cases = [
        [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
        [[3,2],[1,0]],
        [[1, 1, 1, 1],[1, 1, 1, 0],[1, 1, 0, -1],[1, 0, -1, -1]],
        [[-1]],
        [[0]],
        [[1]],
        [[1] * 5,] * 5 + [[0] * 5,] * 2 + [[-1] * 5,] * 5
        
    ]
    for grid in test_cases:
        result = solution.countNegatives(grid)
        print(grid, result)


if __name__ == "__main__":
    main()
