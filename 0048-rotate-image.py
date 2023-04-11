''' https://leetcode.com/problems/rotate-image/
'''

class Solution:
    def rotate(self, matrix):

        def swap4(i, j):
            ''' Swap clock-wise 4 pixel at the i j coordinate
            '''
            # Coordinates to swap
            x = (i, j,  -i-1, -j-1)
            y = (j, -i-1,  -j-1,  i)

            # The swap
            matrix[x[0]][y[0]], matrix[x[3]][y[3]], matrix[x[2]][y[2]], matrix[x[1]][y[1]] = \
                matrix[x[3]][y[3]], matrix[x[2]][y[2]], matrix[x[1]][y[1]], matrix[x[0]][y[0]]
            

        size = len(matrix)

        # Do the move for a "wedge" shaped segment of the matrix
        for row in range((size)//2):
            for col in range(row, size-row - 1):
                swap4(row, col)

        return None


    # Original, more readable version of swap4
        # def swap4(i, j):
        #     ''' Swap clock-wise 4 pixel at the i j coordinate
        #     '''
        #     # Coordinates to move
        #     x = (i, j,  -i-1, -j-1)
        #     y = (j, -i-1,  -j-1,  i)

        #     # Keep the first one in a buffer
        #     buffer = matrix[i][j]

        #     # Do three moves
        #     for to, frm in ((0, 3),(3, 2), (2, 1)):
        #         matrix[x[to]][y[to]] = matrix[x[frm]][y[frm]]
            
        #     # Restore the last one from the buffer
        #     matrix[x[1]][y[1]] = buffer

def make_square(size):
    ''' Make a square matrix size "size"
    '''
    result = []
    count = 1
    for _ in range(size):
        result.append([])
        for _2 in range(size):
            result[-1].append(count)
            count += 1
    return result
    
def main():
    ''' Test rotate
    '''

    def print_matrix(matrix):
        maxlen = len(str(max((max(line) for line in matrix))))
        print(maxlen)
        for line in matrix:
            print(" ".join([str(i).rjust(maxlen, " ") for i in line]))

    solution = Solution()

    test_cases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        make_square(5),
        #[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ]
    for matrix in test_cases:
        print("IN")
        print_matrix(matrix)
        solution.rotate(matrix)
        print("OUT")
        print_matrix(matrix)

def big_case(size=100):
    solution = Solution()
    matrix = make_square(size)
    start = time.time()
    solution.rotate(matrix)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    big_case(2000)