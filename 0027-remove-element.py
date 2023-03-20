''' https://leetcode.com/problems/remove-element/
'''

class Solution:
    # A lot of this is copied from 0026
    def removeElement(self, nums, val):

        # Pointer to write non-val results
        copy_to = 0
        # Candidate for the next non-val elements
        copy_from = 0


        while copy_from < len(nums):

            # If it is not the "forbidden" value
            if nums[copy_from] != val:

                # Copy it into the next slot and update copy_to
                nums[copy_to] = nums[copy_from]
                copy_to += 1

            # Move the pointer
            copy_from += 1

        # Number of found elements is pointer + 1
        return copy_to
    

def main():
    ''' Test removeElement
    '''
    solution = Solution()

    test_cases = [
        ([1], 1),
        ([1], 2),
        ([1, 2], 1),
        ([1, 1], 1),
        ([1, 1], 2),
        ([1,1,2,2,3,3,4,5,6,7,7,], 2),
    ]
    for nums, val in test_cases:
        print(f"IN: {nums}", val)
        k = solution.removeElement(nums, val)
        print(f"OUT: {nums}, {k}")
        print()

if __name__ == "__main__":
    main()