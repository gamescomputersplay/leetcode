''' https://leetcode.com/problems/lucky-numbers-in-a-matrix/
'''

class Solution:
    def luckyNumbers (self, matrix):

        rows_mins = [float("inf") for _ in range(len(matrix))]
        cols_maxs = [float("-inf") for _ in range(len(matrix[0]))]

        for row_n, row in enumerate(matrix):
            for col_n, element in enumerate(row):
                rows_mins[row_n] = min(rows_mins[row_n], element)
                cols_maxs[col_n] = max(cols_maxs[col_n], element)

        return list(set(rows_mins).intersection(set(cols_maxs)))


def main():
    ''' Test luckyNumbers
    '''
    solution = Solution()

    test_cases = [
        [[3,7,8],[9,11,13],[15,16,17]],
        [[1,10,4,2],[9,3,8,7],[15,16,17,12]],
        [[7,8],[1,2]],
        [[0]],
    ]
    for matrix in test_cases:
        result = solution.luckyNumbers(matrix)
        print(matrix, result)



if __name__ == "__main__":
    main()
