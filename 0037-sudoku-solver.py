''' https://leetcode.com/problems/sudoku-solver/
'''

class Solution:
    def solveSudoku(self, board):

        def is_valid(i, j):
            ''' Check attempt matrix: does placing number in i j
            results in valid sudoku?
            '''
            number = attempt[i][j]
            for n in range(9):
                if attempt[n][j] == number and n != i:
                    return False
                if attempt[i][n] == number and n != j:
                    return False
                x, y = i//3*3 + n%3, j//3*3 + n//3
                #print(n, x, y)
                if attempt[x][y] == number and x != i and y != j:
                    return False
            return True

        # Create a work copy with lists of options in empty cells

        options = []
        attempt = []

        for i in range(9):
            options.append([])
            attempt.append([])
            for j in range(9):
                if board[i][j] != ".":
                    options[-1].append(board[i][j])
                    attempt[-1].append(board[i][j])
                else:
                    options[-1].append([str(i) for i in range(1, 10)])
                    attempt[-1].append(".")

        #print(options)

        # Backtracking stack. It will contain backtracking point as:
        # [(i, j, index of element to try), ...]
        stack = []

        i, j = 0, 0

        for _ in range(100000):

            

            # This is to move to the next line when appropriate 
            if j == 9:
                i += 1
                j =0
            # If we passed through all rows - break from the while
            if i == 9:
                break

            # We are at back tracking point
            if stack and (i, j) == stack[-1][:2]:

                # Pop the stack value
                stack_i, stack_j, stack_attempt = stack.pop()
                # If the next attempt does not exist: remove this backtracking point
                if stack_attempt > len(options[i][j]) - 1:
                    attempt[i][j] = "."
                    i, j, _ = stack[-1]
                    # print(f"Exhausted all option, going back to {i}, {j}")
                    continue

                # If the attempt valid - try next one
                attempt[i][j] = options[i][j][stack_attempt]
                # print(f"Trying value {options[i][j][stack_attempt]}, at {i} {j}")
                stack.append((i, j, stack_attempt + 1))

                # Move on if valid
                if is_valid(i, j):
                    j += 1

            # If the options are fixed number - ignore it and move on
            elif not isinstance(options[i][j], list):
                # print(i, j, options[i][j])
                j += 1

            # If options are a list: set a back tracking point
            else:
                # print(f"Set backtracking point at {i}, {j}")
                stack.append((i, j, 0))

        print(attempt)

        return

def main(verbose=True):
    ''' Test solveSudoku
    '''
    solution = Solution()

    test_cases = [
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
        [[".",".","4","6","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
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
