''' https://leetcode.com/problems/summary-ranges/
'''

class Solution:
    def summaryRanges(self, nums):


        ranges = []
        start = None

        p = 0

        while p < len(nums):

            if start is None:
                start = nums[p]

            if p == len(nums) - 1 or nums[p+1] - nums[p] > 1:
                ranges.append(str(start) if nums[p] == start else f"{start}->{nums[p]}")
                start = None

            p += 1

        return ranges


def main():
    ''' Test searchInsert
    '''
    solution = Solution()

    test_cases = [
        [0,1,2,4,5,7],
        [0,2,3,4,6,8,9],
        [],
        [1],
        [1, 2],
        [1, 3],
    ]
    for nums in test_cases:
        result = solution.summaryRanges(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
