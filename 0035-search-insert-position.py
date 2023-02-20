''' https://leetcode.com/problems/search-insert-position/
'''

class Solution:
    def searchInsert(self, nums, target):
        ''' Find a place to insert target into a sorted list nums
        '''

        left = 0
        right = len(nums)

        while True:

            middle = (left + right) // 2
            # print(left, middle, right)

            if nums[middle] == target:
                return middle
            if right - left == 1:
                return right if nums[middle] < target else left

            if nums[middle] < target:
                left = middle
            else:
                right = middle


        return right

def main():
    ''' Test searchInsert
    '''
    solution = Solution()

    test_cases = [
        ([1,3,5,6], 5),
        ([1,3,5,6], 2),
        ([1,3,5,6], 7),
        ([1], 1), 
        ([1], 2),
        ([1], 0),
        ([1, 3], 0), 
        ([1, 3], 1), 
        ([1, 3], 2),
        ([1, 3], 3),
        ([1, 3], 4),
    ]
    for array, target in test_cases:
        print(array, target, solution.searchInsert(array, target))

if __name__ == "__main__":
    main()
