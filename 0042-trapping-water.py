''' https://leetcode.com/problems/trapping-rain-water/
'''

class Solution:
    def trap(self, height):

        # Max wall from the right
        max_right = []
        for wall in height[::-1]:
            if not max_right:
                max_right.append(wall)
            elif wall > max_right[-1]:
                max_right.append(wall)
            else:
                max_right.append(max_right[-1])

        # Calculate Max wall from the left and water at the same time

        max_left = 0
        water = 0

        for pos, wall in enumerate(height):
            if max_left == 0:
                max_left = wall
            elif wall > max_left:
                max_left = wall

            water += min(max_left, max_right[-pos-1]) - wall

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
        [0,1,0,2,1,0,1,3,2,1,2,1]*10000, 

    ]
    for height in test_cases:
        result = solution.trap(height)
        print(height[:20], result)


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    elapsed = time.time() - start
    print(elapsed)