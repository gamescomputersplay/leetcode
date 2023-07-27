''' https://leetcode.com/problems/container-with-most-water/
'''

class Solution:

    def maxArea(self, height):
        ''' Another attempt at the problem.
        '''

        def find_best_wall(arr, val):
            ''' Find first value that is equal or higher
            '''
            left = 0
            right = len(arr)

            while True:
                center = (left + right) // 2
                if center == 0:
                    return arr[0]
                if left == len(arr) - 1:
                    return arr[len(arr) - 1]
                if arr[center][0] >= val > arr[center-1][0]:
                    return arr[center]
                if arr[center][0] < val:
                    left = center
                else:
                    right = center
  
        # Stack of walls, each one higher that the previous one,
        # with their positions: [(height, position), ...]
        left_walls = []

        # Go through the walls
        for position, wall in enumerate(height):

            # Populate the stack (only add the wall
            # that is higher than the last in stack)
            if (not left_walls or wall > left_walls[-1][0]) and wall > 0:
                left_walls.append((wall, position))

        # Same for the right walls
        right_walls = []
        for position, wall in enumerate(height[::-1]):
            if (not right_walls or wall > right_walls[-1][0]) and wall > 0:
                right_walls.append((wall, len(height) - position - 1))

        max_water = 0
        for one_side, other_side in [(left_walls, right_walls), (right_walls, left_walls)]:
            for one_wall in one_side:

                # in the right wall stack,
                # find first from the right that is equal of higher

                other_wall = find_best_wall(other_side, one_wall[0])
                water = abs(other_wall[1] - one_wall[1]) * min(other_wall[0], one_wall[0])
                max_water = max(max_water, water)

        return max_water


    def maxArea_bestMemory(self, height):
        ''' Return the max volume of water
        Firt accepted attempt. Bad timing, great memory
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

        # Same for teh right walls
        right_walls = []
        for position, wall in enumerate(height[::-1]):
            if (not right_walls or wall > right_walls[-1][0]) and wall > 0:
                right_walls.append((wall, len(height) - position - 1))


        max_water = 0

        for left_wall, left_position in left_walls:

            half_mark = len(right_walls) // 2

            # Minimal distance (for pruning)
            min_distance = max_water / left_wall

            for right_wall, right_position in right_walls[half_mark:]:

                # This wall is too close to surpass teh max_water
                if right_position - left_position < min_distance:
                    break

                water = min(left_wall, right_wall) * \
                    (right_position - left_position)

                # Recalculate min_distance each time we have new record
                if water > max_water:
                    max_water = water
                    min_distance = max_water / left_wall

            min_height = max_water / (len(height) - left_position)

            for right_wall, right_position in right_walls[:half_mark + 1][::-1]:

                # This wall is too close to surpass the max_water
                if right_wall < min_height:
                    break

                water = min(left_wall, right_wall) * \
                    (right_position - left_position)

                # Recalculate min_distance each time we have new record
                if water > max_water:
                    max_water = water
                    min_height = max_water / (len(height) - left_position)

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
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
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
    test_one_case()
    main()
    test_random_case()
    test_large_case()

