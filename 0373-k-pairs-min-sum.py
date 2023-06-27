''' https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
'''

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):

        result = []
        candidates = []

        layer = 0
        while layer + 1 < len(nums1) + len(nums2) and len(result) < k:

            # Add new layer of candidates
            for i in range(layer + 1):
                if i < len(nums1) and layer-i < len(nums2):
                    candidates.append((
                        nums1[i], nums2[layer-i], # numbers
                        nums1[i] + nums2[layer-i], # their sum
                        layer)) # layer they are taken from
            
            #print(f"Layer {layer}, candidates: {candidates}")

            # Sort candidates
            candidates.sort(key=lambda x: x[2])

            # Add candidates to the result, until you find one on the edge
            # meaning p1 + p2 == layer
            used_candidate = 0
            for i, candidate in enumerate(candidates):
                used_candidate += 1
                result.append(candidate[:2])
                if candidate[3] == layer or len(result) == k:
                    break

            # Trim candidates
            candidates = candidates[used_candidate:]

            # And expand to the next layer
            layer += 1

        return result

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
