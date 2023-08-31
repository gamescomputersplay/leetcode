''' https://leetcode.com/problems/triangle/
'''

class Solution:
    def minimumTotal(self, triangle):

        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    triangle[row][col] += triangle[row - 1][0]
                elif col == len(triangle[row]) - 1:
                    triangle[row][col] += triangle[row - 1][-1]
                else:
                    triangle[row][col] += min(triangle[row - 1][col - 1], triangle[row - 1][col])
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
