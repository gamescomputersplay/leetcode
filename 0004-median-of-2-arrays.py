''' https://leetcode.com/problems/median-of-two-sorted-arrays/
'''


class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


def main():
    ''' Test findMedianSortedArrays
    '''
    solution = Solution()

    test_cases = [
       ([1, 3], [2]), # 2
       ([1, 2], [3, 4]), # 2.5
       ([1, 2, 3, 4], [5, 6, 7, 8]), # 5.5
    ]
    for list1, list2 in test_cases:
        print(solution.findMedianSortedArrays(list1, list2))

if __name__ == "__main__":
    main()
