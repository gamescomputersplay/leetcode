''' https://leetcode.com/problems/maximum-length-of-pair-chain/
'''

class Solution:
    def findLongestChain(self, pairs):

        pairs.sort()

        curr_end = pairs[0][1]
        pair_count = 1

        for start, end in pairs[1:]:

            if end < curr_end:
                curr_end = end
            elif start > curr_end:
                curr_end = end
                pair_count += 1

        return pair_count


def main():
    ''' Test findLongestChain
    '''
    solution = Solution()

    test_cases = [
        [[1,2],[2,3],[3,4]], #2
        [[1,2],[7,8],[4,5]], #3
    ]
    for nums in test_cases:
        result = solution.findLongestChain(nums)
        print(f"{nums}, {result}")

if __name__ == "__main__":
    main()
