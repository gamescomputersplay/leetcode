''' https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''

class Solution:
    def kWeakestRows(self, mat, k):
        weakest = []
        ignore = set()
        col = 0
        while True:
            for n, row in enumerate(mat):
                if row[col] == 0 and n not in ignore:
                    weakest.append(n)
                    ignore.add(n)
                    if len(weakest) == k:
                        return weakest
            col += 1
            if col == len(mat[0]):
                break
        row = 0
        while len(weakest) < k:
            if row not in ignore:
                weakest.append(row)
                ignore.add(row)
            row += 1
        return weakest

def main():
    ''' Test kWeakestRows
    '''
    solution = Solution()

    test_cases = [
        (   [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]], 3),

        (   [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]], 2),
        ([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 2),
        ([[1,0],[1,0],[1,0],[1,1]], 4),
    ]
    for mat, k in test_cases:
        result = solution.kWeakestRows(mat, k)
        print(mat, k, result)


if __name__ == "__main__":
    main()
