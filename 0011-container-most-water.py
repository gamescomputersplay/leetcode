''' https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height):
        ''' Return the max volume of water
        '''

        # Stack of walls, each one higher that the previous one,
        # with their positions: [(height, position), ...]
        rising_walls = []

        max_water = float("-inf")

        # Go through the walls
        for position, wall in enumerate(height):

            # Find the most water volume between current wall
            # and the walls in the stack
            for left_wall_height, left_wall_position in rising_walls:

                water = min(left_wall_height, wall) * \
                    (position - left_wall_position)
                max_water = max(max_water, water)

                # If left wall is higher than current wall, no need
                # to check the rest they will be smaller
                if left_wall_height > wall:
                    break

            # Populate the stack (only add the wall
            # that is higher than the last in stack)
            if not rising_walls or wall > rising_walls[-1][0]:
                rising_walls.append((wall, position))

        return max_water

    def maxAreaBrute(self, height):
        ''' Same with brute force
        '''
        max_water = 0

        for pos1, wall1 in enumerate(height):
            for pos2, wall2 in enumerate(height):
                if pos2 <= pos1:
                    continue
                water = (pos2 - pos1) * min(wall1, wall2)
                max_water = max(max_water, water)

        return max_water

def random_case(size):
    ''' Gerenate a random case size "size"
    '''
    case = []
    for i in range(size):
        case.append(random.randint(0, size * 2))
    return case

def main():
    ''' test maxArea
    '''
    test_cases = [
        [1, 3, 2, 5, 3, 8, 3, 4], #?
        [1, 8, 6, 2, 5, 4, 8, 3, 7], #49
        [1, 1], #1
    ]

    solution = Solution()
    for array in test_cases:
        print()
        print(array, solution.maxArea(array), solution.maxAreaBrute(array))

def test_random_case():
    ''' Test random cases with bruteforce
    '''
    random_cases = [random_case(i) for i in range(2, 101)]
    solution = Solution()
    for array in random_cases:
        if solution.maxArea(array) != solution.maxAreaBrute(array):
            print("Error")
            print("Test case: ", array)
            break
    else:
        print(f"{len(random_cases)} tested, all okay")

def test_large_case():
    ''' The one that cases the timeout
    '''
    solution = Solution()
    for power in range(2, 15):
        size = 2**power
        large_case = [i for i in range(size//2)] + [i for i in range(size//2, -1, -1)]
        start = time.time()
        result = solution.maxArea(large_case)
        # print(result)
        elapsed = time.time() - start
        print(f"Power: {power}. Size {len(large_case)}. Done in {elapsed}s")

if __name__ == "__main__":
    import random
    import time
    #main()
    #test_random_case()
    test_large_case()
