''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''

class Solution:
    def findMin(self, nums):

        # Remove duplicates from the end
        # Also take care of "all the same" situation
        while nums[-1] == nums[0]:
            if len(nums) == 1:
                return nums[0]
            nums.pop()

        # This happens if array is rotated to itself
        if nums[-1] > nums[0]:
            return nums[0]

        # Set let as the last non-repeating element from the left
        left = 0
        while nums[left] == nums[left + 1]:
            left += 1

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
        [1,3,5],
        [2,2,2,0,1],
    ]
    for nums in test_cases:
        result = solution.findMin(nums)
        print(f"{nums}: {result}")

def random_tests(runs=10):
    solution = Solution()
    for _ in range(runs):
        array = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        array = sorted(list(array))
        for _ in range(random.randint(0, 10)):
            array = [array[-1]] + array[:-1]
        #print(array)
        result = solution.findMin(array)
        if result != min(array):
            print(f"Fail at: {array}")
            return
    print(f"{runs} random tests okay")


if __name__ == "__main__":
    import random
    main()
    random_tests(10000)
