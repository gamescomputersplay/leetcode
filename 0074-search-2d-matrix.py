''' https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    def searchMatrix(self, matrix, target):

        def flat_addr(addr):
            return matrix[addr//cols][addr%cols]

        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows * cols - 1

        if target in (flat_addr(left), flat_addr(right)):
            return True

        while True:

            center = (left + right) // 2
            center_value = flat_addr(center)
            if center_value == target:
                return True
            if right - left <= 1:
                return False

            if center_value > target:
                right = center
            else:
                left = center

def main():
    ''' Test searchMatrix
    '''

    solution = Solution()

    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
        ([[1, 2, 3, 5, 6, 7]], 0),
        ([[1, 2, 3, 5, 6, 7]], 1),
        ([[1, 2, 3, 5, 6, 7]], 3),
        ([[1, 2, 3, 5, 6, 7]], 4),
        ([[1, 2, 3, 5, 6, 7]], 7),
        ([[1, 2, 3, 5, 6, 7]], 8),
        ([[0]], 0),
        ([[0]], 1),
        ([[1, 2]], 0),
        ([[1, 2]], 1),
        ([[1, 2]], 2),
        ([[1, 2]], 3),

    ]

    for matrix, target in test_cases:
        result = solution.searchMatrix(matrix, target)
        print(matrix, target, result)

if __name__ == "__main__":
    main()