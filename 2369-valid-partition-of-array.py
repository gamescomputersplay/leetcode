''' https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
'''

class Solution:
    def validPartition(self, nums):

        # Can subarray division start at this position
        can_start_here = [True] + [False] * len(nums)

        for i in range(len(nums) - 1):

            # Only continue if there are valid subarray divisions at this point
            if not can_start_here[i]:
                continue

            # This is (1,1) rule
            if nums[i] == nums[i+1]:
                can_start_here[i+2] = True

            if i >= len(nums)-2:
                continue

            # This is (1,1,1) rule
            if nums[i] == nums[i+1] and nums[i+2] == nums[i+1]:
                can_start_here[i+3] = True

            # This is (1,2,3) rule
            elif nums[i] + 1 == nums[i+1] and nums[i+2] == nums[i+1] + 1:
                can_start_here[i+3] = True

        return can_start_here[-1]

def main():
    ''' Test validPartition
    '''
    solution = Solution()

    test_cases = [
        [4,4,4,5,6],
        [1,1,1,2],
    ]
    for array in test_cases:

        result = solution.validPartition(array)
        print(array, result)

if __name__ == "__main__":
    main()
