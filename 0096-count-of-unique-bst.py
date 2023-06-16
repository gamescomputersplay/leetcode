''' https://leetcode.com/problems/unique-binary-search-trees/
'''

class Solution:

    def __init__(self):
        self.cache = {}

    def numTrees(self, n):

        if n in self.cache:
            return self.cache[n]

        # End of recursion, only 1 option with 0 or 1 nodes
        if n < 2:
            return 1

        count_varuants = 0

        # iterate through size of the left branch
        # Which can be 0 to n-1
        for n_left in range(n):

            n_right = n - n_left - 1

            count_varuants += self.numTrees(n_left) * self.numTrees(n_right)

        self.cache[n] = count_varuants
        
        return count_varuants

def main():
    ''' Test numTrees
    '''
    solution = Solution()

    test_cases = [
       n for n in range(1, 20)
    ]
    for n in test_cases:
        result = solution.numTrees(n)
        print(f"{n}: {result}")

if __name__ == "__main__":
    main()
