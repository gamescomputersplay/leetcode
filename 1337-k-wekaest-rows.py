''' https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''

class Solution:
    def kWeakestRows(self, mat, k):
        sums = [(sum(row), n) for n, row in enumerate(mat)]
        sums.sort()
        return [n for _, n in sums[:k]]

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
    ]
    for mat, k in test_cases:
        result = solution.kWeakestRows(mat, k)
        print(mat, k, result)


if __name__ == "__main__":
    main()
