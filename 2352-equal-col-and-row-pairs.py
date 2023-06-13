''' https://leetcode.com/problems/equal-row-and-column-pairs/
'''

class Solution:
    def equalPairs(self, grid):

        size = len(grid)

        # 1. Generate hashes of all cols
        col_hashes = {}

        for n in range(size):

            col = []
            for row in grid:
                col.append(str(row[n]))

            col_hash = hash("|".join(col))
            col_hashes[col_hash] = col_hashes.get(col_hash, 0) + 1

        # 2. Go through rows and sum up hash hits
        matches = 0

        for row in grid:
            row_hash = hash("|".join([str(n) for n in row]))
            matches += col_hashes.get(row_hash, 0)

        return matches
    
def main():
    ''' Test equalPairs
    '''
    solution = Solution()

    test_cases = [
        [[3,2,1],[1,7,6],[2,7,7]], #1
        [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], #3
        [[1]]
    ]
    for array in test_cases:

        result = solution.equalPairs(array)
        print(array, result)

if __name__ == "__main__":
    main()
