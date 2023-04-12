''' https://leetcode.com/problems/n-queens/
'''

# Almost identical to 0051

class Solution:
    def totalNQueens(self, n):

        def is_safe(positions):
            ''' Check if current position is legit.
            Only the last queen i snew, so only check her
            '''
            # Quick test: if numbers are not unique position is not legit
            if len(set(positions)) != len(positions):
                return False
            
            # Look at all previous queens
            for col, position in enumerate(positions[:-1]):

                # Vertical shift from the last column, if go diagonally
                diag_shift = len(positions) - col - 1

                # Does the queen in this column has the same coordinate as
                # the last queen (also if diagonal shift added/removed)
                if position in (-diag_shift + positions[-1], diag_shift + positions[-1]):
                    return False

            return True

        # Track "Queens so far" and "next row to test"
        stack = [[0]]
        solution_count = 0

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
                    solution_count += 1
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

        return solution_count


def main():
    ''' Test totalNQueens
    '''
    solution = Solution()

    test_cases = [i for i in range(1, 10)]
    for n in test_cases:
        result = solution.totalNQueens(n)
        print(f"{n} {result}")

def big_case(size=11):
    solution = Solution()
    start = time.time()
    solution.totalNQueens(size)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    big_case()
