''' https://leetcode.com/problems/single-element-in-a-sorted-array/
'''

class Solution:
    def singleNonDuplicate(self, nums):

        # Setup edges of binary search
        left = 0
        right = len(nums)
        middle = (left + right) // 2

        while True:

            # Check if we found the guy
            # That is:
            # 1. it is at the end and the only neighbor is a different number
            # 2. it is in between two different numbers
            if (middle == 0 or nums[middle - 1] != nums[middle]) and \
                (middle == len(nums) - 1 or nums[middle + 1] != nums[middle]):
                break 

            # mid is even 0, 2, 4 and the right neighbor is equal OR
            # mid is odd 1, 3, 5 and the left neighbor is equal:
            # the goal is on the right from middle
            if middle % 2 == 0 and nums[middle - 1] != nums[middle] or \
                middle % 2 == 1 and nums[middle + 1] != nums[middle]:
                left = middle
            else:
                right = middle

            middle = (left + right) // 2

        return nums[middle]


def main():
    ''' Test searchInsert
    '''
    solution = Solution()

    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1], 1),
        ([1, 1, 2], 2),
        ([1, 2, 2], 1),
        ([1, 1, 2, 3, 3], 2),
    ]
    for array, answer in test_cases:
        result = solution.singleNonDuplicate(array)
        print(array, result, result == answer)



if __name__ == "__main__":
    main()