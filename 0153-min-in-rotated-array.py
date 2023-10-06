''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution:
    def findMin(self, nums):

        # Array rotated into itself
        # This also covers array len=1
        if nums[0] <= nums[-1]:
            return nums[0]            

        left = 0
        right = len(nums)

        while True:

            center = (left + right) // 2

            if center > 0 and nums[center] < nums[center - 1]:
                return nums[center]

            if nums[center] > nums[0]:
                left = center
            else:
                right = center


def main():
    ''' Test findMin
    '''
    solution = Solution()

    test_cases = [
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
    ]
    for nums in test_cases:
        result = solution.findMin(nums)
        print(f"{nums}: {result}")

def random_tests(runs=10):
    solution = Solution()
    for _ in range(runs):
        array = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        array = sorted(list(set(array)))
        for _ in range(random.randint(0, 10)):
            array = [array[-1]] + array[:-1]
        # print(array)
        result = solution.findMin(array)
        if result != min(array):
            print(f"Fail at: {array}")
            return
    print(f"{runs} random tests okay")


if __name__ == "__main__":
    import random
    main()
    random_tests(10000)