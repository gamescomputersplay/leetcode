''' https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m, n):

        matrix = []
        
        for i in range(m):

            matrix.append([])

            for j in range(n):

                if i == 0 and j == 0:
                    matrix[-1].append(1)

                elif i == 0:
                    matrix[-1].append(matrix[i][j-1])

                elif j == 0:
                    matrix[-1].append(matrix[i-1][j])
                    
                else:
                    matrix[-1].append(matrix[i-1][j] + matrix[i][j-1])

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

if __name__ == "__main__":
    main()