''' https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums):

        solution = set()
        nums.sort()

        lookup = {}
        for num in nums[1:]:
            lookup[num] = lookup.get(num, 0) + 1

        for i, num1 in enumerate(nums[1:-1], start=1):
            lookup[num1] -= 1
            for num2 in nums[:i]:

                if -num1-num2 in lookup and lookup[-num1-num2] > 0:
                    solution.add((num2, num1, -num2-num1))

        return list(solution)

    def threeSum_brute(self, nums):
        solution = set()
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                for k, num3 in enumerate(nums):
                    if i != j and j != k and k != i and \
                       num1 + num2 + num3 == 0:
                        solution.add(tuple(sorted([num1, num2, num3])))
        return [list(item) for item in sorted(solution)]


def main():
    ''' Test threeSum
    '''
    solution = Solution()

    test_cases = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
    ]
    for nums in test_cases:
        result = solution.threeSum(nums)
        result_brute = solution.threeSum_brute(nums)
        print(nums, result_brute, result)

def random_test(runs=100):
    ''' Run random test, check correctness with bruteforce
    '''
    solution = Solution()

    for _ in range(runs):
        nums = [random.randint(-5, 5) for _ in range(random.randint(3, 10))]
        result = solution.threeSum(nums)
        result = [list(item) for item in sorted(result)]
        result_brute = solution.threeSum_brute(nums)
        if result_brute != result:
            print(f"Error on: {nums}")
            print(f"Result: {result}")
            print(f"Brute result: {result_brute}")
            return
    print(f"{runs} random tests okay")
    return
            
def large_case(case_size):
    ''' Time the large case
    '''
    nums = [random.randint(-10000, 10000) for i in range(case_size)]
    solution = Solution()
    start = time.time()
    solution.threeSum(nums)
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
    random_test(10000)
    test_timing(13)
