''' https://leetcode.com/problems/knight-probability-in-chessboard/
'''

class Solution:
    def knightProbability(self, n, k, row, column):

        # No moves
        if k == 0:
            return 1

        # Board's too small
        if n < 3:
            return 0

        # Initiate the board
        board = [[0] * n for _ in range(n)]
        board[row][column] = 1

        moves = [(1, -2), (-1, 2), (-1, -2), (1, 2), (-2, 1), (2, -1), (-2, -1), (2, 1)]

        # Moved
        for _ in range(k):

            # Board for the next move
            new_board = [[0] * n for _ in range(n)]

            # Go through existing board's cells
            for i, row in enumerate(board):
                for j, cell in enumerate(row):

                    if cell == 0:
                        continue

                    # Calculate next moves
                    for di, dj in moves:

                        # Calculate new cell after the move
                        if 0 <= i + di < n and 0 <= j + dj < n:
                            new_board[i + di][j + dj] += cell / 8

            board = new_board

        # Sum all the values of the board
        remaining_chance = sum(sum(cell for cell in row) for row in board)

        return remaining_chance

def main():
    ''' Test knightProbability
    '''
    solution = Solution()

    test_cases = [
        (3, 2, 0, 0), #0.0625
        (1, 0, 0, 0), #1
    ]
    for n, k, row, column in test_cases:
        result = solution.knightProbability(n, k, row, column)
        print(f"{n}, {k}, {row}, {column}, {result}")

if __name__ == "__main__":
    main()