''' https://leetcode.com/problems/3sum-closest/
'''

class Solution:
    def threeSumClosest(self, nums, target):
        return 0

def main():
    ''' Test threeSumClosest
    '''
    solution = Solution()

    test_cases = [
        ([-1, 2, 1, -4], 1), #2
        ([0,0,0], 1), #0
    ]
    for nums, target in test_cases:
        result = solution.threeSumClosest(nums, target)
        print(nums, target, result)

def large_case(case_size):
    ''' Time the large case
    '''
    nums = [random.randint(-10000, 10000) for i in range(case_size)]
    target = random.randint(-10000, 10000)
    solution = Solution()
    start = time.time()
    solution.threeSumClosest(nums, target)
    elapsed = time.time() - start
    return elapsed

def test_timing(max_power = 12):
    ''' Run a series of ever larger cases
    '''
    for power in range(2, max_power):
        size = 2**power
        elapsed = large_case(size)
        print(F"{power}:{size} {elapsed}")

if __name__ == "__main__":
    import random
    import time
    main()
    #test_timing()
