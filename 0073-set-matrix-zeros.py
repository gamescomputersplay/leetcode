''' https://leetcode.com/problems/set-matrix-zeroes/
'''

class Solution:
    def setZeroes(self, matrix):

        # Track which rows and cols need to be zeroed
        zero_rows = set()
        zero_cols = set()

        # Determine which rows and cols conain zeros
        for row, line in enumerate(matrix):
            for col, element in enumerate(line):
                if element == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Set zeroes in the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col in zero_cols or row in zero_rows:
                    matrix[row][col] = 0

        return None


def main():
    ''' Test setZeroes
    '''

    def print_matrix(matrix):
        for line in matrix:
            string_line = [str(num) for num in line]
            print(" ".join(string_line))
        print()
    
    solution = Solution()

    test_cases = [
        [[1,1,1],[1,0,1],[1,1,1]],
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
    ]

    for matrix in test_cases:
        print("IN:")
        print_matrix(matrix)
        solution.setZeroes(matrix)
        print("OUT:")
        print_matrix(matrix)

if __name__ == "__main__":
    main()