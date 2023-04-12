''' https://leetcode.com/problems/permutations/
'''

class Solution:
    def permute(self, nums):

        if len(nums) == 1:
            return [[nums[0]]]

        result = []

        for num in nums:

            new_nums = nums.copy()
            new_nums.remove(num)

            for perm in self.permute(new_nums):
                perm.extend([num])
                result.append(perm)

        return result
    
def main():
    ''' Test permute
    '''
    solution = Solution()

    test_cases = [[j+1 for j in range(i)] for i in range(1, 7)]
    for nums in test_cases:
        result = solution.permute(nums)
        print(nums, len(result), result[:10])

def big_case(size=10):
    solution = Solution()
    nums = [j+1 for j in range(size)]
    start = time.time()
    solution.permute(nums)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    big_case(9)
