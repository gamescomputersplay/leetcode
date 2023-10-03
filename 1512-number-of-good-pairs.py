''' https://leetcode.com/problems/number-of-good-pairs/
'''

class Solution:
    def numIdenticalPairs(self, nums):

        freq = {}
        pairs = 0
        for num in nums:
            if num in freq:
                pairs += freq[num]
                freq[num]  += 1
            else:
                freq[num] = 1

        return pairs

def main():
    ''' Test numIdenticalPairs
    '''
    solution = Solution()

    test_cases = [
        [1,2,3,1,1,3], #4
        [1,1,1,1], #6
        [1,2,3], #0
    ]
    for nums in test_cases:
        result = solution.numIdenticalPairs(nums)
        print(nums, result)


if __name__ == "__main__":
    main()
