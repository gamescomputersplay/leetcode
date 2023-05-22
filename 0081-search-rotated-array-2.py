''' https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''

class Solution:
    # I gave up and just used deduplication + search if it was unique
    
    def search(self, nums, target):

        def binary_search(first, last):
            ''' Search in the segment nums[first: last],
            assuming there are no rotation.
            It is assumed that last > first (meaning the segment is not empty)
            '''

            left, right = first, last

            while True:

                center = (left + right) // 2

                if unums[center] == target:
                    return True

                if unums[center] > target and (center == first or unums[center - 1] < target):
                    return False
                if unums[center] < target and (center == last - 1 or unums[center + 1] > target):
                    return False

                if unums[center] > target:
                    right = center
                else:
                    left = center 

        # Deduplicate the nums array
        unums = [num for i, num in enumerate(nums) if i==0 or num != nums[i-1]]
        if len(unums) > 1 and unums[0] == unums[-1]:
            unums.pop()

        # First, check that the array was rotated at all
        # "=" will also cover 1-element array
        if unums[-1] >= unums[0]:
            return binary_search(0, len(unums))

        # Find the rotation point (first element of the right part)
        left, right = 0, len(unums)
        while True:

            center = (left + right) // 2

            if center < len(unums) - 2 and unums[center] > unums[center + 1]:
                rotation = center + 1
                break

            if center > 0 and unums[center] < unums[center - 1]:
                rotation = center
                break

            if unums[center] < unums[-1]:
                right = center
            else:
                left = center 

        if unums[0] <= target:
            return binary_search(0, rotation)

        return binary_search(rotation, len(unums))



def main():
    ''' Test search
    '''
    solution = Solution()

    test_cases = [
       ([2,5,6,0,0,1,2], 0),
       ([2,5,6,0,0,1,2], 3),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 1),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 2),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 3),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 4),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 5),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 6),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 7),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 8),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 9),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 10),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 0),
       ([6, 7, 8, 9, 10, 1], 0),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 11),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 7.5),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 3.5),
       ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 5.5),
        ([1,0,1,1,1], 0),
        [(3, 1), 3],
        ([3, 5, 1], 0),
        #([-9,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-6,-5,-5,-4,-4,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-2,-1,-1,-1,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,9,9,9,9,10,10,10,10,-10,-10,-10,-10,-10,-10,-9,-9,-9], 13)
    ]

    for nums, target in test_cases:
        result = solution.search(nums, target)
        print(nums, target, result)

if __name__ == "__main__":
    main()
