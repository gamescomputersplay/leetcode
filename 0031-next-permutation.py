''' https://leetcode.com/problems/next-permutation/
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        # Go through the elements back to front (element I)
        for i in range(len(nums)-1, -1, -1):

            # For each element look to the left
            for j in range(i-1, -1, -1):

                # Find a place where numbers go UP (element J)
                if nums[j] < nums[j + 1]:

                    # To the right of J find a minimal number that is
                    # bigger than J (element K)
                    min_value = None
                    min_pos = None
                    for k in range(j+1, len(nums)):
                        if nums[k] > nums[j]:
                            if min_value is None or nums[k] < min_value:
                                min_value = nums[k]
                                min_pos = k



                    # And switch those elements (J and K)
                    nums[min_pos], nums[j] = nums[j], nums[min_pos]

                    # Finally, sort ascending everything to the right of J
                    nums[j+1:] = sorted(nums[j+1:])

                    # Done for this case
                    return
        
        # If no J element found - we are in the very last permutation
        # Sort all array asc
        nums[:] = sorted(nums[:])


def main():
    ''' Test nextPermutation
    '''
    solution = Solution()

    test_cases = [
        [1,2,3],
        [3,2,1],
        [1,1,5],
        [1, 3, 4, 2],
        [1], 
        [1,1,1,1]
    ]
    for test_case in test_cases:
        print(f"IN: {test_case}")
        solution.nextPermutation(test_case)
        print(f"OUT: {test_case}\n")

def full_circle(nums):
    solution = Solution()
    original = nums.copy()
    print(nums)
    solution.nextPermutation(nums)
    while nums != original:
        print(nums)
        solution.nextPermutation(nums)
    print()


if __name__ == "__main__":
    main()
    full_circle([1, 2, 3, 4])
    full_circle([1, 1, 2, 2])
