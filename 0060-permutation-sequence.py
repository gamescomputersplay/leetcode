''' https://leetcode.com/problems/permutation-sequence/
'''

class Solution:
    def getPermutation(self, n, k):

        # We'll need factorials
        factorials = [1, 1]
        for i in range(9):
            factorials.append(factorials[-1] * len(factorials))

        # And the list of items sequence is made of
        numbers = [str(n) for n in range(1, n+1)]

        result = []

        # Pick the resulting string one-by-one from left
        for i in range(n):
            
            # Length of a chunk where the number in this position is the same
            partition_length = factorials[len(numbers) - 1]
             # And which number in the list should be be?
            partition = (k - 1) // partition_length

            # Get the number from the list and add to the result
            result.append(numbers[partition])
            # Remove it from the list
            del numbers[partition]
            # Adjust K accordingly
            k %= partition_length

        return "".join(result)
    

def main():
    ''' Test getPermutation
    '''
    solution = Solution()

    test_cases = [
        (3, 3), # 213
        (4, 9), # 2314
        (3, 1), # 123
        (9, 100_000),
        (1, 1),
        (2, 2),
    ]
    for n, k in test_cases:
        result = solution.getPermutation(n, k)
        print(n, k, result)

if __name__ == "__main__":
    main()