''' https://leetcode.com/problems/champagne-tower/
'''

class Solution:
    def champagneTower(self, poured, query_row, query_glass):

        # How much wine are already in the glasses
        wine = [[0] * (n + 1) for n in range(query_row + 1)]
        # Pour all teh wine in the top glass
        wine[0][0] = poured

        # Trickle it down row by row, glass by glass
        for row_n, row in enumerate(wine):
            for glass_n, glass in enumerate(row):

                # Wherever there is overflow
                if glass > 1:
                    # Trickle it to the row below
                    # (but ignore rows beyond query_row)
                    if row_n + 1 <= query_row:
                        wine[row_n + 1][glass_n] += (glass - 1) / 2
                        wine[row_n + 1][glass_n + 1] += (glass - 1) / 2
                    # And set overflown glass to 1
                    wine[row_n][glass_n] = 1
        #print(wine)

        return wine[query_row][query_glass]

def main():
    ''' Test champagneTower
    '''
    solution = Solution()

    test_cases = [
        (1, 1, 1), # 0
        (2, 1, 1), # 0.5
        (100000009, 33, 17), # 1
    ]
    for poured, query_row, query_glass in test_cases:
        result = solution.champagneTower(poured, query_row, query_glass)
        print(f"{poured}, {query_row}, {query_glass}: {result}")

if __name__ == "__main__":
    main()
