''' https://leetcode.com/problems/valid-sudoku/
'''

class Solution:
    def isValidSudoku(self, board):

        # Rows
        houses = [[(i, j) for j in range(9)] for i in range(9)]
        # Columns
        houses += [[(j, i) for j in range(9)] for i in range(9)]
        # Squares
        houses += [[(j//3 + i//3 * 3, j%3 + i%3 * 3) for j in range(9)] for i in range(9)]

        # Go through the houses
        for house in houses:

            # And check uniqueness of the numbers
            already = set()
            for i, j in house:

                if board[i][j] == ".":
                    continue
                if board[i][j] in already:
                    return False
                already.add(board[i][j])

        return True

def main():
    ''' Test isValidSudoku
    '''
    solution = Solution()

    test_cases = [
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]], # True

[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]], # False
    ]
    for sudoku in test_cases:
        result = solution.isValidSudoku(sudoku)
        print(result)


if __name__ == "__main__":
    main()