''' https://leetcode.com/problems/spiral-matrix/
'''

class Solution:
    def spiralOrder(self, matrix):

        # Output
        output = []
        # Track visited to know when to turn
        visited = set()
        size_x, size_y =  len(matrix), len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        x, y = 0, 0

        # Keep going until all numbers  were read
        while True:

            # Append the result, and track which coordinate were used
            output.append(matrix[x][y])
            if len(output) == size_x * size_y:
                break
            visited.add((x, y))

            # Find the next direction to go / coordinate based on
            # - it is not an edge
            # - it has not been visited
            while True:

                dx, dy = directions[direction]
                next_x, next_y = x + dx, y + dy

                if 0 <= next_x < size_x and 0 <= next_y < size_y and (next_x, next_y) not in visited:
                     x, y =  next_x, next_y
                     break

                direction += 1
                direction %= 4

        return output

def make_rect(x, y):
    ''' Make a rectangle matrix size "size"
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
        [[1,1,1],[1,1,1],[1,1,1]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        make_rect(6, 5),
        make_rect(1, 1),
        make_rect(1, 10),
        make_rect(10, 1),
        
    ]
    for matrix in test_cases:
        print("IN")
        print_matrix(matrix)
        result = solution.spiralOrder(matrix)
        print(result)

if __name__ == "__main__":
    main()