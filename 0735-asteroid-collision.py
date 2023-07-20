''' https://leetcode.com/problems/asteroid-collision/
'''

class Solution:
    def asteroidCollision(self, asteroids):
        result = [asteroids[0]]

        for asteroid in asteroids[1:]:

            # Flying right - just add to stack
            if asteroid > 0:
                result.append(asteroid)
                continue

            # Flying left - fight it out with stack
            while result and result[-1] > 0:

                # Different outcomes
                # break means negative asteroid exploded
                # pop means positive asteroid destoid
                if abs(asteroid) > result[-1]:
                    result.pop()
                elif abs(asteroid) == result[-1]:
                    result.pop()
                    break
                elif abs(asteroid) < result[-1]:
                    break

            # If negative was not destoed (no breaks), add it to the stack
            else:
                result.append(asteroid)

        return result

def main():
    ''' Test asteroidCollision
    '''
    solution = Solution()

    test_cases = [
        [5,10,-5],
        [8, -8],
        [10,2,-5],
        [2,3,-4,-2,11,4,5,-3,-9]
    ]
    for asteroids in test_cases:
        result = solution.asteroidCollision(asteroids)
        print(f"{asteroids}, {result}")

if __name__ == "__main__":
    main()