''' https://leetcode.com/problems/surrounded-regions/
'''

class Solution:
    def solve(self, board):

        # Regions touching the border mark as "S"
        stack = []
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == "O":
                    board[i][j] = "S"
                    stack.append((i, j))
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "S"
                    stack.append((i, j))

        # Flood fill S-regions
        while stack:

            i, j = stack.pop()
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                    if board[i + di][j + dj] == "O":
                        board[i + di][j + dj] = "S"
                        stack.append((i + di, j + dj))

        # Replace all "O" to "X" and all "S" to "O":
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

        return None

def main():
    ''' Test solve
    '''
    solution = Solution()

    test_cases = [
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X"]],
        [["O"]],
        [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]],
    ]
    for board in test_cases:
        print("IN ", board)
        solution.solve(board)
        print("OUT", board)
        print()


if __name__ == "__main__":
    main()