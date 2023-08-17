''' https://leetcode.com/problems/01-matrix/
'''

class Solution:
    def updateMatrix(self, mat):

        def check_cell(x, y):
            mindist = float("inf")
            original_value = mat[x][y]

            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                newx, newy = x + dx, y + dy
                if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]):
                    mindist = min(mindist, mat[newx][newy] + 1)

            if mindist == original_value:
                return

            mat[x][y] = mindist
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                newx, newy = x + dx, y + dy
                if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]):
                    todo.append((newx, newy))

        #todo = [(i, j) for i in range(len(mat)) for j in range(len(mat[0]))]
        todo = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    todo.append((i,j))
                    mat[i][j] = float("inf")

        while todo:
            x, y = todo.pop()
            if mat[x][y] != 0:
                check_cell(x, y)

        return mat

def main():
    ''' Test updateMatrix
    '''
    solution = Solution()

    test_cases = [
        [[0,0,0],[0,1,0],[0,0,0],[0,1,1],[1,1,1]],
        [[0,0,0],[0,1,0],[1,1,1]],
        [[0]],
        [[0,1]],
        [[1]*99 + [0]]
    ]
    for mat in test_cases:
        print(f"IN: {mat}")
        result = solution.updateMatrix(mat)
        print(f"OUT: {result}")



if __name__ == "__main__":
    main()