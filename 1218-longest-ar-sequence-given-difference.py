''' https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
'''

class Solution:
    def longestSubsequence(self, arr, difference):

        # dict to track sequinses as:
        # {next_item: length_so_far}
        seqs = {}

        for num in arr:

            # We've been waiting for this number since one of the previous sequinces
            if num in seqs:

                # Next number to wait
                new_num = num + difference
                # Sequence lenths
                new_count = seqs[num] + 1

                # Don't wait previous number anymore
                del seqs[num]
                # Wait for new number
                # (and if there is one already, track the longest length)
                seqs[new_num] = max(seqs.get(new_num, 0), new_count)

            # Start tracking new sequence (if we don't wait for this number already)
            elif num + difference not in seqs:
                seqs[num + difference] = 1

        return max(seqs.values())

def main():
    ''' Test longestSubsequence
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4], 1), #4
        ([1,3,5,7], 1), #1
        ([1,5,7,8,5,3,4,2,1], -2), #4
        ([3,4,1,2,3], 1), #3
        ([1], 100), #1
        ([7,-2,8,10,6,18,9,-8,-5,18,13,-6,-17,-1,-6,-9,9,9], 1), #3

    ]
    for arr, difference in test_cases:
        result = solution.longestSubsequence(arr, difference)
        print(arr, difference, result)


if __name__ == "__main__":
    main()
