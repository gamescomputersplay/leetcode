''' https://leetcode.com/problems/sort-colors/
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers to swap 0s and 2s into
        p0 = 0
        p2 = len(nums) - 1

        i = 0

        while True:

            # Keep swapping while there are 2s
            while nums[i] == 2 and p2 > i:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

            # Or 0s
            while nums[i] == 0 and p0 < i:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

            # When we reached where pointer 2 is, we are done
            if p2 == i:
                break

            i += 1

        return None

def main():
    ''' Test sortColors
    '''

    solution = Solution()

    test_cases = [

        [2,0,2,1,1,0],
        [2,0,1],
        [0],
        [1],
        [2],
        [1, 0],
        [2, 1],
        [2, 1],
        [2, 0],
        [1, 2, 0],
        [1, 1, 1, 2, 0],
        [1, 1, 1, 2, 0],
        [1, 2, 0, 2, 0],
        [1, 2, 0, 2, 2],
    ]

    for nums in test_cases:
        print(f"IN: {nums}")
        solution.sortColors(nums)
        print(f"OUT: {nums}\n")

if __name__ == "__main__":
    main()