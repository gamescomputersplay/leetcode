''' https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
'''

class Solution:
    def minimumReplacement(self, nums):

        # Array of 1 is sorted already
        if len(nums) == 1:
            return 0

        # replacement counter
        replacements = 0

        # Look at al elements right to left,
        # starting from the second to last
        for i in range(len(nums)-2, -1, -1):

            # The element is out of sort
            # (needs to be broken down)
            if nums[i] > nums[i+1]:

                # The number of chunks to break into is ceiling of (i // i+1)
                if nums[i] % nums[i+1] == 0:
                    parts = nums[i] // nums[i+1]
                else:
                    parts = (nums[i] // nums[i+1]) + 1

                # parts-1 is the number of breaks
                replacements += parts - 1

                # What's the highest of the last part we can provide
                new_height = nums[i] // parts

                # That would become a new hight to affect the next number
                nums[i] = new_height

        return replacements

def main():
    ''' Test minimumReplacement
    '''
    solution = Solution()

    test_cases = [
        [3,9,3], # 2
        [1,2,3,4,5], # 0
        [5, 4, 3, 2, 1], # 10
        [5, 19, 6]
    ]
    for nums in test_cases:

        result = solution.minimumReplacement(nums)
        print(nums, result)

if __name__ == "__main__":
    main()
