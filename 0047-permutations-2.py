''' https://leetcode.com/problems/permutations-ii/
'''

# Similar tp 0046, but with a few extra lines - see comments

class Solution:

    def __init__(self):
        self.cache = {}

    def permuteUnique(self, nums):

        if tuple(nums) in self.cache:
            return self.cache[tuple(nums)]

        if len(nums) == 1:
            self.cache[tuple(nums)] = [[nums[0]]]
            return [[nums[0]]]

        # Use set to filter duplicates
        result = set()

        for num in nums:

            new_nums = nums.copy()
            new_nums.remove(num)

            for perm in self.permuteUnique(new_nums):

                # Use tuples to be able to use in a set
                perm = list(perm)
                perm.extend([num])
                result.add(tuple(perm))

        results = list(result)
        self.cache[tuple(nums)] = results
        return results
    
def main():
    ''' Test permuteUnique
    '''
    solution = Solution()

    test_cases = [
        [1,1,1],
        [1,1,2],
        [1,2,3],
        [1,2,3] * 2,
    ]
    for nums in test_cases:
        result = solution.permuteUnique(nums)
        print(nums, len(result), result[:10])

def big_case(size=5):
    solution = Solution()
    nums = [j+1 for j in range(size)] * 2
    start = time.time()
    solution.permuteUnique(nums)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    big_case(5)
