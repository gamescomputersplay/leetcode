''' https://leetcode.com/problems/median-of-two-sorted-arrays/
'''


class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def regular_median(array):
            ''' Return a median of a sorted array
            '''
            if len(array) % 2 == 0:
                return (array[len(array) // 2] + array[(len(array) // 2) - 1]) / 2
            return float(array[len(array) // 2])

        # Sanitizing: one of the inputs is empty
        # (assuming that at least one of them isn't)
        if not nums1:
            return regular_median(nums2)
        if not nums2:
            return regular_median(nums1)

def main():
    ''' Test findMedianSortedArrays
    '''
    solution = Solution()

    test_cases = [
        ([1, 3, 5], []), # 3
        ([], [1, 2, 3, 4]), # 2.5
        # ([1, 3, 5, 7], [2, 4, 6, 8]), # 4.5
        # ([1, 3], [2]), # 2
        # ([1, 2], [3, 4]), # 2.5
        # ([1, 2, 3, 4], [5, 6, 7, 8]), # 5.5
    ]
    for list1, list2 in test_cases:
        print(solution.findMedianSortedArrays(list1, list2))

if __name__ == "__main__":
    main()
