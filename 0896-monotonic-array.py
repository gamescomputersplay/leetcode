''' https://leetcode.com/problems/monotonic-array/
'''

class Solution:
    def isMonotonic(self, nums):

        goes_up = False
        goes_down = False
        prev = nums[0]

        for num in nums[1:]:
            if num > prev:
                goes_up = True
            elif num < prev:
                goes_down = True
            prev = num
            if goes_up and goes_down:
                return False

        return not (goes_up and goes_down)

def main():
    ''' Test isMonotonic
    '''
    solution = Solution()

    test_cases = [
        [1,2,2,3],
        [6,5,4,4],
        [1,3,2],
        [1],
        [1,2],
    ]
    for nums in test_cases:
        result = solution.isMonotonic(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
