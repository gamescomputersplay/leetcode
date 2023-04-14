''' https://leetcode.com/problems/spiral-matrix/
'''

class Solution:
    def spiralOrder(self, matrix):

        output = []
        size_x, size_y =  len(matrix), len(matrix[0]),

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0

        for line_n in range(min(size_x, size_y) * 2):

            line_length = (size_y, size_x)[line_n%2] - 1 - line_n // 4 * 2
            dx, dy = directions[line_n%4]
            print(line_length, dx, dy)

            for i in range(line_length):
                #print(x, y)
                output.append(matrix[x][y])
                x += dx
                y += dy
 
        return output

def make_square(x, y):
    ''' Make a square matrix size "size"
    '''
    result = []
    count = 1
    for _ in range(y):
        result.append([])
        for _2 in range(x):
            result[-1].append(count)
            count += 1
    return result

def print_matrix(matrix):
    maxlen = len(str(max((max(line) for line in matrix))))

    for line in matrix:
        print(" ".join([str(i).rjust(maxlen, " ") for i in line]))

def main():
    ''' Test maxSubArray
    '''
    solution = Solution()

    test_cases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        make_square(6, 5)
    ]
    for matrix in test_cases:
        print("IN")
        print_matrix(matrix)
        result = solution.spiralOrder(matrix)
        print(result)

if __name__ == "__main__":
    import random
    main()