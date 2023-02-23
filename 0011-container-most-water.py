''' https://leetcode.com/problems/container-with-most-water/
'''

class Solution:

    def maxArea(self, height):
        ''' Return the max volume of water
        '''

        # Stack of walls, each one higher that the previous one,
        # with their positions: [(height, position), ...]
        left_walls = []
        # Go through the walls
        for position, wall in enumerate(height):

            # Populate the stack (only add the wall
            # that is higher than the last in stack)
            if (not left_walls or wall > left_walls[-1][0]) and wall > 0:
                left_walls.append((wall, position))

        #print(left_walls)

        # Same for teh right walls
        right_walls = []
        for position, wall in enumerate(height[::-1]):
            if (not right_walls or wall > right_walls[-1][0]) and wall > 0:
                right_walls.append((wall, len(height) - position - 1))
        #print(right_walls)

        max_water = 0

        for left_wall, left_position in left_walls:
            
            # Minimal distance (for pruning)
            min_distance = max_water / left_wall

            for right_wall, right_position in right_walls:
                
                # This wall is too close to surpass teh max_water
                if right_position - left_position < min_distance:
                    break

                water = min(left_wall, right_wall) * \
                    (right_position - left_position)

                # Recalculate min_distance each time we have new record
                if water > max_water:
                    max_water = water
                    min_distance = max_water / left_wall

        return max_water


    def maxAreaFailed(self, height):
        ''' Return the max volume of water
        '''

        def measure_water(left_wall, right_wall):
            return min(left_wall[0], right_wall[0]) * (right_wall[1] - left_wall[1])

        # Stack of walls, each one higher that the previous one,
        # with their positions: [(height, position), ...]
        rising_walls = []

        max_water = float("-inf")

        # Go through the walls
        for position, wall in enumerate(height):

            # Find the max volume of water between "wall" and any
            # of the walls in the stack
            right_wall = (wall, position)
            print(rising_walls, right_wall)

            # If there are few elements, simply go through them
            if len(rising_walls) < 3:
                for left_wall in rising_walls:
                    water = measure_water(left_wall, right_wall)
                    max_water = max(max_water, water)
            # Otherwise, let's use binary  search
            else:
                left = 0
                right = len(rising_walls) - 1
                middle = (left + right) // 2

                while True:

                    print(left, middle, right)
                    step_left = -1 if middle == 0 else measure_water(rising_walls[middle - 1], right_wall)
                    step_right = -1 if middle == len(rising_walls) - 1 else measure_water(rising_walls[middle + 1], right_wall)
                    middle_water = measure_water(rising_walls[middle], right_wall)
                    print(step_left, middle_water, step_right)
                    if right - left < 2:
                        water = max(step_left, middle_water, step_right)
                        break
                    if step_left < middle_water and step_right < middle_water:
                        water = middle_water
                        break

                    if step_left < step_right:
                        left = middle
                    else:
                        right = middle
                    middle = (left + right) // 2

                max_water = max(max_water, water)
                print(max_water)

            # Populate the stack (only add the wall
            # that is higher than the last in stack)
            if not rising_walls or wall > rising_walls[-1][0]:
                rising_walls.append((wall, position))

        return max_water

    def maxAreaSlow(self, height):
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
    ''' test maxArea with manual cases
    '''
    test_cases = [
        [1, 3, 2, 5, 3, 8, 3, 4], # 18
        [1, 8, 6, 2, 5, 4, 8, 3, 7], # 49
        [0, 0], # 0
        [0, 1], # 0
        [1, 1], # 1
        [3, 10, 6, 15, 16, 15, 13, 2], #?
        [17, 26, 18, 39, 19, 22, 38, 34, 39, 37, 47, 35, 38, 19, 20, 17, 1, 6, 36, 48, 7, 9, 39, 7, 14], 
        [9, 16, 23, 1, 10, 18, 17, 2, 16, 4, 25, 1, 26],
        [1, 8, 2, 8, 12, 20, 17, 2, 15, 13, 15],
    ]

    solution = Solution()
    for array in test_cases:
        print(array, solution.maxArea(array), solution.maxAreaBrute(array))

def test_one_case():
    ''' test maxArea for one case
    '''
    array = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]
    solution = Solution()
    print(array, solution.maxArea(array), solution.maxAreaBrute(array))


def test_random_case():
    ''' Test random cases with bruteforce
    '''
    random_cases = [random_case(i) for i in range(2, 101)]
    solution = Solution()
    for array in random_cases:
        #print(array)
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
        #print(large_case)
        start = time.time()
        result = solution.maxArea(large_case)
        # print(result)
        elapsed = time.time() - start
        print(f"Power: {power}. Size {len(large_case)}. Done in {elapsed}s")

if __name__ == "__main__":
    import random
    import time
    #test_one_case()
    #main()
    #test_random_case()
    test_large_case()
