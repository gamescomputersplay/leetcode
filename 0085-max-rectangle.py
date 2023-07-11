''' https://leetcode.com/problems/maximal-rectangle/
'''

class Solution:
    def maximalRectangle(self, matrix):

        def max_rect_in_hist(row):
            ''' Max rectangle in a histogram row'''
            stack = []
            max_area = 0
            for pos, height in enumerate(row + [0]):

                while stack and stack[-1][0] > height:
                    h, p = stack.pop()
                    if stack:
                        width = pos - stack[-1][1] - 1
                    else:
                        width = pos
                    max_area = max(max_area, width * h)

                stack.append((height, pos))
            return max_area

        # Create a matrix that counts all the filled cells above current one (including current one)
        above = [[0 for _ in range(len(matrix[0]))]]
        for row in matrix:
            above.append([(int(curr) + prev) * int(curr) for curr, prev in zip(row, above[-1])])

        print(above)

        # For each line in that matrix, do "Largest rectangle in a histogram"

        max_area = 0
        for row in above:
            max_area = max(max_area, max_rect_in_hist(row))
        return max_area


def main():
    ''' Test maximalRectangle
    '''
    solution = Solution()

    test_cases = [
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
        [["0"]],
        [["1"]],
    ]
    for matrix in test_cases:
        result = solution.maximalRectangle(matrix)
        print(f"{matrix}, {result}")


if __name__ == "__main__":
    main()
