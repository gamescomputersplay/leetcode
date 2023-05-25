''' https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

### This is very similar to 0026, only one line is different

class Solution:
    def removeDuplicates(self, nums):

        # Last unique elements we found
        copy_to = 0
        # Candidate for the next unique elements
        copy_from = 1


        while copy_from < len(nums):

            # Unique elements found
            # This is the only line that was changed
            if copy_to < 1 or nums[copy_from] != nums[copy_to-1]:
                # Copy it into the next slot and update copy_to
                copy_to += 1
                nums[copy_to] = nums[copy_from]

            # Move the pointer
            copy_from += 1

        # Number of found elements is pointer + 1
        return copy_to + 1

def main():
    ''' Test removeDuplicates
    '''
    solution = Solution()

    test_cases = [
        [1],
        [1, 1],
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 2],
        [1, 2, 2],
        [1, 2, 2, 2],
        [1,1,2,2,2,2,3,3,3,4,5,6,6,6,6,7,7,],
    ]
    for test_case in test_cases:
        print(f"IN: {test_case}")
        k = solution.removeDuplicates(test_case)
        print(f"OUT: {test_case}, {k}")
        print()

if __name__ == "__main__":
    main()