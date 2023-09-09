''' https://leetcode.com/problems/combination-sum-iv/
'''

class Solution:
    def combinationSum4(self, nums, target):

        def rec_count(remaining):
            ''' Count combinations for remaining amount
            '''
            if remaining in cache:
                return cache[remaining]
            ways = 0
            for num in nums:
                new_remaining = remaining - num
                if new_remaining == 0:
                    ways += 1
                elif remaining < 0:
                    pass
                else:
                    ways += rec_count(new_remaining)
            cache[remaining] = ways
            return ways

        cache = {}

        return rec_count(target)

def main():
    ''' Test combinationSum4
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3], 4),
        ([1,1,2,2,3,3,1,3], 100),
        ([9], 3),
    ]
    for nums, target in test_cases:
        result = solution.combinationSum4(nums, target)
        print(f"{nums}, {target}: {result}")

if __name__ == "__main__":
    main()
        