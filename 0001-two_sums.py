''' https://leetcode.com/problems/two-sum/
'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Set will contain the difference to target for each number
        missing = set()

        # Go through all the numbers
        for position, number in enumerate(nums):

            # Did we see the difference just like this number
            if number in missing:
                # If we did, calculate which numbers were those
                return [nums.index(target - number), position]

            # Add the difference to the set
            missing.add(target - number)


def main():
    ''' Test the twoSum
    '''
    test_cases = [
        ([2, 7, 11, 15], 9),  # [0, 1]
        ([3, 2, 4], 6),  # [1, 2]
        ([3, 3], 6),  # [0, 1]
        ([-1,-2,-3,-4,-5], -8)
    ]

    solution = Solution()
    for nums, target in test_cases:
        print(solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
