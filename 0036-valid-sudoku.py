''' https://leetcode.com/problems/valid-sudoku/
'''

class Solution:
    def isValidSudoku(self, board):

        # Go through the houses
        for i in range(9):

            # Row
            house = [board[i][j] for j in range(9) if board[i][j] != "."]
            if len(house) != len(set(house)):
                return False
            
            # Column
            house = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(house) != len(set(house)):
                return False
            
            # Square
            x, y = i//3 * 3, i%3 * 3
            house = [board[j//3 + x][j%3 + y] for j in range(9) if board[j//3 + x][j%3 + y] != "."]
            if len(house) != len(set(house)):
                return False

        return True

def main(verbose=True):
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
        if verbose:
            print(result)

def timing():
    start = time.time()
    for _ in range(10000):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    timing()