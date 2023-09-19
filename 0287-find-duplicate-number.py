''' https://leetcode.com/problems/find-the-duplicate-number/
'''

class Solution:
    def findDuplicate(self, nums):

        def count_range(beg, end):
            count = 0
            for num in nums:
                if beg <= num <= end:
                    count += 1
            return count
        
        left = 1
        right = len(nums) - 1

        while True:

            center = (left + right) // 2

            if left == right:
                return left
            if count_range(left, center) > center - left + 1:
                right = center
            else:
                left = center + 1

def generate_random_test(limit=10):
    n = random.randint(1, limit)
    target = random.randint(1, n)
    nums = list(range(1, n + 1))
    nums.append(target)
    for _ in range(random.randint(0, limit)):
        nums[random.randint(0, len(nums)-1)] = target
    return nums, target

def random_tests(runs):
    solution = Solution()
    for _ in range(runs):
        nums, target = generate_random_test()
        result = solution.findDuplicate(nums)
        if result != target:
            print(f"Error on {nums}: result = {result}, expected = {target}")
            break
    else:
        print(f"{runs} random tests okay")


def main():
    ''' Test findDuplicate
    '''
    solution = Solution()

    test_cases = [
        [1,3,4,2,2],
        [3,1,3,4,2],
        [1,1],
        [1,2,3,4,5,6,7,8,9,4],
        [2,2,2,2,2],
        [1,2,3,4,5,4,7,8,9,4],
    ]

    for nums in test_cases:
        result = solution.findDuplicate(nums)
        print(nums, result)

if __name__ == "__main__":
    import random
    main()
    random_tests(10000)
