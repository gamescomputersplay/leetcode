''' https://leetcode.com/problems/two-sum/
'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Sort the input data
        nums_sorted = sorted(nums)

        # Initiate 2 pointers
        low, high = 0, len(nums) - 1

        # Initiate current sum (smallest + largest)
        current_sum = nums_sorted[low] + nums_sorted[high]

        # Assumption was there is a solution,
        # so we don't need to worry that this never happens
        while current_sum != target:

            # Depending on which way we off, either increase
            # the low number or decrease the high number
            if current_sum < target:
                low += 1
            elif current_sum > target:
                high -= 1

            current_sum = nums_sorted[low] + nums_sorted[high]

        # The answer is the position of those number in the original list
        first = nums.index(nums_sorted[low])
        # This is to make sure it is not the same index
        second = nums.index(nums_sorted[high], first + 1)
        
        return [first, second]


def main():
    ''' Test the twoSum
    '''
    test_cases = [
        ([2, 7, 11, 15], 9),  # [0, 1]
        ([3, 2, 4], 6),  # [1, 2]
        ([3, 3], 6),  # [0, 1]
    ]

    solution = Solution()
    for nums, target in test_cases:
        print(solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
