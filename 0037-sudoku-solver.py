''' https://leetcode.com/problems/sudoku-solver/
'''

class Solution:
    def solveSudoku(self, board):

        def is_valid(i, j):
            ''' Check attempt matrix: does placing number in i j
            results in valid sudoku?
            '''
            number = board[i][j]
            for n in range(9):
                if board[n][j] == number and n != i:
                    return False
                if board[i][n] == number and n != j:
                    return False
                x, y = house_map[(i,j)][n]
                if board[x][y] == number and x != i and y != j:
                    return False
            return True

        # Helper to optimize checking houses
        house_map = {}
        for i in range(9):
            for j in range(9):
                house_map[(i,j)] = []
                for n in range(9):
                    house_map[(i,j)].append((i//3*3 + n%3, j//3*3 + n//3))

        # Numbers already present in rows and cols
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        houses = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):  
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    house_n = i//3 * 3 + j//3
                    houses[house_n].add(board[i][j])

        # Dict of cells and their options
        options = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    house_n = i//3 * 3 + j//3
                    possible_options = set((str(i) for i in range(1, 10))) - \
                                       rows[i] - cols[j] - houses[house_n]
                    # If there is only one option - write it down
                    if len(possible_options) == 1:
                        board[i][j] = possible_options.pop()
                    # Otherwise -- keep the list of options
                    else:
                        options[(i, j)] = list(possible_options)


        # Backtracking stack. It will contain backtracking point as:
        # [(i, j, index of next element to try), ...]
        stack = []

        # Go through all the cells
        i, j = 0, 0
        while True:

            # This is to move to the next line when appropriate 
            if j == 9:
                i += 1
                j =0

            # If we passed through all rows - break from the while, we are done
            if i == 9:
                break

            # We are at back tracking point
            if stack and (i, j) == stack[-1][:2]:

                # Pop the stack value
                stack_i, stack_j, stack_attempt = stack.pop()
                # If the next attempt does not exist: remove this backtracking point
                if stack_attempt > len(options[(i, j)]) - 1:
                    board[i][j] = "."
                    i, j, _ = stack[-1]
                    # print(f"Exhausted all option, going back to {i}, {j}")
                    continue

                # If the attempt valid - try next one
                board[i][j] = options[(i, j)][stack_attempt]
                # print(f"Trying value {options[i][j][stack_attempt]}, at {i} {j}")
                stack.append((i, j, stack_attempt + 1))

                # Move on if valid
                if is_valid(i, j):
                    j += 1

            # If the options are fixed number - ignore it and move on
            elif (i, j) not in options:
                # print(i, j, options[i][j])
                j += 1

            # If options are a list: set a back tracking point
            else:
                # print(f"Set backtracking point at {i}, {j}")
                stack.append((i, j, 0))

        return

def main(verbose=True):
    ''' Test solveSudoku
    '''
    solution = Solution()

    test_cases = [
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
        # [[".",".","4","6","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ]
    for sudoku in test_cases:
        if verbose:
            print("IN")
            for line in sudoku:
                print(" ".join(line))
        solution.solveSudoku(sudoku)
        if verbose:
            print("OUT")
            for line in sudoku:
                print(" ".join(line))

def timing():
    start = time.time()
    for _ in range(30):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    timing()
