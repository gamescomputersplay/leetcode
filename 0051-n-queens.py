''' https://leetcode.com/problems/n-queens/
'''

class Solution:
    def solveNQueens(self, n):

        def is_safe(positions):
            ''' Check if current position is legit.
            Only the last queen i snew, so only check her
            '''
            # Look at all previous queens
            for col, position in enumerate(positions[:-1]):

                # Vertical shift from the last column, if go diagonally
                diag_shift = len(positions) - col - 1

                # Does the queen in this column has the same coordinate as
                # the last queen (also if diagonal shift added/removed)
                if position in (-diag_shift + positions[-1], positions[-1], diag_shift + positions[-1]):
                    return False
            return True

        # Track "Queens so far" and "next row to test"
        stack = [[0]]
        result = []

        while stack:

            # Next position to test is out of bounds, backtrack
            if stack[-1][-1] == n:
                stack.pop()
                continue

            #print(stack, is_safe(stack[-1]))

            # Last queen is legit
            if is_safe(stack[-1]):

                # Solution is long enough:
                # save a copy of it and continue
                if len(stack) == n:
                    result.append(stack[-1].copy())
                    stack[-1][-1] += 1

                
                else:
                    # Create a fork:
                    # 1. Continue with the current queen later
                    stack[-1][-1] += 1
                    # 2 Add new queen for right now
                    new_queen = stack[-1].copy()
                    new_queen[-1] -= 1
                    new_queen.extend([0])
                    stack.append(new_queen)
            
            # Queen is not legit - next row
            else:
                stack[-1][-1] += 1

        # Transform the result to  match the requirements
        # (it rotates the solution clockwise, but it's okay)
        return [["." * q + "Q" + "." * (n-q-1) for q in solution] for solution in result]


def main():
    ''' Test solveNQueens
    '''
    solution = Solution()

    test_cases = [i for i in range(1, 10)]
    for n in test_cases:
        result = solution.solveNQueens(n)
        print(f"{n}:{len(result)} {result[:5]}")

if __name__ == "__main__":
    main()