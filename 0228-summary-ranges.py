''' https://leetcode.com/problems/summary-ranges/
'''

class Solution:
    def summaryRanges(self, nums):

        range_start = None
        range_end = None

        ranges = []

        for element in nums:

            if range_start is not None:

                if element - range_end == 1:
                    range_end = element

                else:
                    ranges.append(str(range_end) if range_end == range_start else f"{range_start}->{range_end}")
                    range_start = None
                    range_end = None

            if range_start is None:
                range_start = element
                range_end = element

        if range_start is not None:
            ranges.append(str(range_end) if range_end == range_start else f"{range_start}->{range_end}")

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
