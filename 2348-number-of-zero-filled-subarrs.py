''' https://leetcode.com/problems/number-of-zero-filled-subarrays/
'''

class Solution:

    def zeroFilledSubarray(self, nums):

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

                # For each new zero in a stretch, just add the current length to the total count
                subarrays_count += zero_count
            else:
                zero_count = 0
                
            previous = num

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
