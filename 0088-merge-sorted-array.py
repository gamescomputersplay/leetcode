''' https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1, m, nums2, n):

        # Move num1 to the back
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        p1, p2, res = n, 0, 0
        both = m + n
        while p1 < both or p2 < n:

            if p2 == n or p1 < both and nums1[p1] <= nums2[p2]:
                nums1[res] = nums1[p1]
                p1 += 1
            else:
                nums1[res] = nums2[p2]
                p2 += 1
            res += 1

        return None

def main():
    ''' Test merge
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,0,0,0], 5, [-2,3,6], 3),
        ([1,2,3,0,0,0], 3, [2,5,6], 3),
        ([1], 1, [], 0),
        ([1, 2, 3], 3, [], 0),
        ([0], 0, [1], 1)
    ]
    for nums1, m, nums2, n in test_cases:
        print(f"IN: {nums1}, {nums2}")
        solution.merge(nums1, m, nums2, n)
        print(f"OUT: {nums1}")
        print()

if __name__ == "__main__":
    main()
