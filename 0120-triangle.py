''' https://leetcode.com/problems/triangle/
'''

class Solution:
    def minimumTotal(self, triangle):

        for row_n, row in enumerate(triangle[1:], start=1):
            for col in range(len(row)):
                if col == 0:
                    row[col] += triangle[row_n - 1][0]
                elif col == len(row) - 1:
                    row[col] += triangle[row_n - 1][-1]
                else:
                    row[col] += min(triangle[row_n - 1][col - 1], triangle[row_n - 1][col])
        return min(triangle[-1])

def main():
    ''' Test connect
    '''
    solution = Solution()

    test_cases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],
        [[-10]]
    ]
    for triangle in test_cases:
        result = solution.minimumTotal(triangle)
        print(f"{triangle}, {result}")

if __name__ == "__main__":
    main()
