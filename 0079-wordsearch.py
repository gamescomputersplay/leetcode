''' https://leetcode.com/problems/word-search/
'''

class Solution:
    def exist(self, board, word):

        def recursive(coords_so_far):
            ''' recursively look for the next letter
            '''
            # End recursion when all letters are found
            if len(coords_so_far) == len(word):
                return True

            # Iterate through four directions:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_x, new_y = coords_so_far[-1]
                new_x, new_y = new_x + dx, new_y + dy

                # Make sure it is withon board and it is not path already taken
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) \
                   and (new_x, new_y) not in coords_so_far:

                    # If the next letter is the next letter of the word
                    if board[new_x][new_y] == word[len(coords_so_far)]:

                        # Go down one level of recursion
                        new_so_far = coords_so_far.copy()
                        new_so_far.append((new_x, new_y))
                        result = recursive(new_so_far)

                        if result:
                            return True

            return False

        # Check if we have enough letters in the matrix
        matrix_content = "".join("".join(c for c in row) for row in board)
        for letter in set(word):
            if word.count(letter) > matrix_content.count(letter):
                return False

        # Find the first letter
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:

                    # initiate recursion starting that letter
                    result = recursive([(i, j)])

                    # Return True if word has been found
                    if result:
                        return True

        return False

def main():
    ''' Test exist
    '''
    solution = Solution()

    test_cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), # True
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), # True
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), # False
        ([["A"]], "A"),
        ([["A"]], "B"),
        ([["A", "C", "C", "A", "C"]], "CCC"),
        ([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAa")
    ]
    for board, word in test_cases:
        result = solution.exist(board, word)
        print(f"{board}, {word}, {result}")


if __name__ == "__main__":
    main()
