''' https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
'''

class Solution:
    def longestSubarray(self, nums):

        # Edge case len == 1
        if len(nums) == 1:
            return 0

        maxarr = 0
        has_zeros = False
        sub1, sub2 = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                sub1 += 1
            if num == 0:
                has_zeros = True
                maxarr = max(maxarr, sub1 + sub2)
                sub1, sub2 = 0, sub1

        # Edge case no zeros
        if not has_zeros:
            return len(nums) - 1

        # check one last time
        maxarr = max(maxarr, sub1 + sub2)

        return maxarr

def main():
    ''' Test longestSubarray
    '''
    solution = Solution()

    test_cases = [
        [1,1,0,1],
        [0,1,1,1,0,1,1,0,1],
        [1,1,1],
        [1],
        [0],
        [0,1],
        [1,0],
        [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
    ]
    for nums in test_cases:
        result = solution.longestSubarray(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
