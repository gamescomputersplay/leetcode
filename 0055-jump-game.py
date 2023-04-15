''' https://leetcode.com/problems/jump-game/
'''

class Solution:
    def canJump(self, nums):

        max_jump = 0

        for pos, num in enumerate(nums):
            if pos > max_jump:
                return False
            max_jump = max(max_jump, pos + num)

        return True

def main():
    ''' Test canJump
    '''
    solution = Solution()

    test_cases = [
        [2,3,1,1,4],
        [3,2,1,0,4],
        [1],
        [0,1]
    ]
    for nums in test_cases:
        result = solution.canJump(nums)
        print(nums, result)

if __name__ == "__main__":
    main()