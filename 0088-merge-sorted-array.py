''' https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        
        return None
    
def main():
    ''' Test merge
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,0,0,0], 3, [2,5,6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1)
    ]
    for nums1, m, nums2, n in test_cases:
        print(nums1, m, nums2, n, solution.merge(nums1, m, nums2, n))

if __name__ == "__main__":
    main()
