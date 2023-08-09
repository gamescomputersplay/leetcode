''' https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
'''

class Solution:
    def minimizeMax(self, nums, p):

        # No different between 0 pair
        if p == 0:
            return 0

        nums.sort()

        # All pair as [(diff, index1, index2)], sorted by diff
        pairs = []
        if p * 2 == len(nums):
            pairs = [(abs(nums[i] - nums[i+1]), i, i+1)
                     for i in range(0, len(nums) - 1, 2)]
        else:
            for distance in range(1, min(10, len(nums))):
                pairs.extend([(abs(nums[i] - nums[i+distance]), i, i+distance)
                            for i in range(len(nums) - distance)])
        pairs.sort(key=lambda x: x[0])

        # Pick p pair from the beginning of the list, suc as none would be overlappiing
        used = set()
        max_pair = 0
        for diff, ind1, ind2 in pairs:
            if ind1 not in used and ind2 not in used:
                max_pair = max(max_pair, diff)
                used.add(ind1)
                used.add(ind2)
                if len(used) == p * 2:
                    return max_pair


def main():
    ''' Test minimizeMax
    '''
    solution = Solution()

    test_cases = [
        ([10,1,2,7,1,3], 2),
        ([4,2,1,2], 1),
        ([-100, 1, 1, 100], 2),
        ([8,9,1,5,4,3,6,4,3,7], 4), # 1
        ([2,6,2,4,2,2,0,2], 4), #2
        ([6,2,8,5,2,4,5], 3), #1 - Fails here
    ]
    for nums, p in test_cases:

        result = solution.minimizeMax(nums, p)
        print(nums, p, result)


if __name__ == "__main__":
    main()
