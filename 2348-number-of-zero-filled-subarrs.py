''' https://leetcode.com/problems/number-of-zero-filled-subarrays/
'''

class Solution:

    def zeroFilledSubarray(self, nums):

        def count_subarrays(zeros):
            ''' How many sub arrays are there in "zeros" zeros
            '''
            if zeros % 2 == 0:
                return (zeros + 1) * (zeros // 2)
            return (zeros + 1) * (zeros // 2) + (zeros // 2 + 1)

        # To keep track of continuous zeros
        previous = None
        # To keep track of the zeros' stretch's length
        zero_count = 0
        # To count subarrays
        subarrays_count = 0

        # Go through the list and identify stretches of continuous zeros
        for num in nums:

            if num == 0:
                if previous is None:
                    zero_count = 1
                else:
                    zero_count += 1
            else:
                if zero_count != 0:
                    subarrays_count += count_subarrays(zero_count)
                zero_count = 0
            previous = num

        if zero_count != 0:
            subarrays_count += count_subarrays(zero_count)

        return subarrays_count

def main():
    ''' Test zeroFilledSubarray
    '''
    solution = Solution()

    test_cases = [
        [1, 3, 0, 0, 2, 0, 0, 4], # 6
        [0, 0, 0, 2, 0, 0], #9
        [2, 10, 2019], #0
        [], # 0
        [0], # 1
        [1], # 0
    ]
    for array in test_cases:

        result = solution.zeroFilledSubarray(array)
        print(array, result)


if __name__ == "__main__":
    main()
