''' https://leetcode.com/problems/sudoku-solver/
'''

class Solution:
    def solveSudoku(self, board):
        return

def main(verbose=True):
    ''' Test solveSudoku
    '''
    solution = Solution()

    test_cases = [
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ]
    for sudoku in test_cases:
        solution.solveSudoku(sudoku)
        if verbose:
            for line in sudoku:
                print(" ".join(line))

def timing():
    start = time.time()
    for _ in range(10000):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    #timing()
