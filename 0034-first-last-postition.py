''' https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

class Solution:
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

        target_start = 0

        # 1. Find the start of target edge

        left = 0
        right = len(nums)

        while True:
        #for _ in range(10):

            center = (left + right) // 2
            #print(left, center, right)

            # Found the beginning in the beginning of the list
            if nums[center] == target and center == 0:
                target_start = center
                break

            # Found the beginning elsewhere
            if nums[center] < target and center <= len(nums) - 2 and nums[center + 1] == target:
                target_start = center + 1
                break

            # There is no beginning (found the gap)
            if nums[center] > target and (center == 0 or nums[center-1] < target):
                target_start = -1
                break

            # There is no beginning (reached right edge)
            if nums[center] < target and center == len(nums) - 1:
                target_start = -1
                break


            if nums[center] >= target:
                right = center
            else:
                left = center

        return [target_start, -1]

def main():
    ''' Test divide
    '''
    solution = Solution()

    test_cases = [
        ([1, 2, 2, 3, 5,7,7,8,8,10], 8),
        ([1,1,1,1,2], 1),
        ([1,1,1,1,2, 2, 2, 2], 2),
        ([1,1,1,1,2], 2),
        ([5,7,7,8,8,10], 6),
        ([1,2,3,4,5], 6),
        ([], 0),


    ]
    for array, target in test_cases:
        result = solution.searchRange(array, target)
        print(array, target, result)


if __name__ == "__main__":
    main()