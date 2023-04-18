''' https://leetcode.com/problems/spiral-matrix-ii/
'''

class Solution:
    def generateMatrix(self, n):

        matrix = [[0 for _1 in range(n)] for _2 in range(n)]

        current_n = 1
        x, y = 0, 0

        side_size = n -1
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        # While there are still numbers to use
        while current_n < n**2:

            # Go through all 4 sides of a circle
            for side in range(4):

                dx, dy = directions[side]

                for position in range(side_size):

                    matrix[x][y] = current_n
                    x += dx
                    y += dy
                    current_n += 1
            
            # One step diagonally to start the next circle
            x += 1
            y += 1
            # Which will be 2 cells smaller in size
            side_size -= 2

        if n%2 == 1:
            matrix[n//2][n//2] = current_n

        return matrix

def print_matrix(matrix):
    maxlen = len(str(max((max(line) for line in matrix))))

    for line in matrix:
        print(" ".join([str(i).rjust(maxlen, " ") for i in line]))

def main():
    ''' Test generateMatrix
    '''
    solution = Solution()

    test_cases = [
        1, 2, 3, 4, 5, 10, 11
        
    ]
    for n in test_cases:
        
        matrix = solution.generateMatrix(n)
        print_matrix(matrix)
        print()

if __name__ == "__main__":
    main()
