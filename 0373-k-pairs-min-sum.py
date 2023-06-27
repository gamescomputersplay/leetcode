''' https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
'''

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):

        candidates = []

        # Steps from the corner (0 is the corner)
        for i in range(min(k, len(nums1) + len(nums2))):
            # Candidates in this step (1, 2, 3)
            for shift in range(i+1):

                if shift < len(nums1) and i-shift < len(nums2):
                    candidates.append((nums1[shift], nums2[i-shift], nums1[shift]+nums2[i-shift]))

        candidates.sort(key=lambda x: x[2])

        return [candidate[:2] for candidate in candidates[:k]]

def main():
    ''' Test kSmallestPairs
    '''
    solution = Solution()

    test_cases = [
        ([1,7,11], [2,4,6], 3),
        ([1,1,2], [1,2,3], 2),
        ([1,2], [3], 3),
        ([1], [3], 100),
        ([1, 2, 3], [4, 5, 6], 10),
    ]

    for nums1, nums2, k in test_cases:
        result = solution.kSmallestPairs(nums1, nums2, k)
        print(nums1, nums2, k, result, "\n")

def large_case():
    solution = Solution()

    nums1 = [i for i in range(1, 10001)]
    nums2 = [i for i in range(1, 10001)]
    k = 10000

    result = solution.kSmallestPairs(nums1, nums2, k)
    print(result[:10], "\n")

if __name__ == "__main__":
    main()
    large_case()
