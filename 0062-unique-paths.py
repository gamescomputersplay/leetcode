''' https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m, n):

        matrix = [[1] * n for _ in range(m)]
        
        for i in range(1, m):

            for j in range(1, n):

                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[-1][-1]
    
def main():
    ''' Test uniquePaths
    '''
    solution = Solution()

    test_cases = [
       (1, 1), 
       (2, 2), 
       (3, 3), 
       (10, 20), 
       (100, 100), 
    ]

    for m, n in test_cases:
        result = solution.uniquePaths(m, n)
        print(m, n, result)

def time_test():
    solution = Solution()
    start = time.time()
    for _ in range(10):
        solution.uniquePaths(1000, 1000)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    time_test()