''' https://leetcode.com/problems/trapping-rain-water/
'''

class Solution:
    def trap(self, height):

        # Max wall from the left

        max_left = []
        for wall in height:
            if not max_left:
                max_left.append(wall)
            elif wall > max_left[-1]:
                max_left.append(wall)
            else:
                max_left.append(max_left[-1])

        #print(max_left)

        # Max wall from the right
        max_right = []
        for wall in height[::-1]:
            if not max_right:
                max_right.append(wall)
            elif wall > max_right[-1]:
                max_right.append(wall)
            else:
                max_right.append(max_right[-1])

        #print(max_right[::-1])

        # Calculate water volume
        water = 0
        for pos, wall in enumerate(height):
            water += min(max_left[pos], max_right[-pos-1]) - wall

        return water

def main():
    ''' Test trap
    '''
    solution = Solution()

    test_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1], # 6
        [4,2,0,3,2,5], # 9
        [1, 2, 3],
        [1],
        [10, 0, 11],
    ]
    for height in test_cases:
        result = solution.trap(height)
        print(height, result)

if __name__ == "__main__":
    import random
    main()
