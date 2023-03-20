''' https://leetcode.com/problems/can-place-flowers/
'''

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # I will mutate input list flowerbed, hope it's okay

        # Do nothing is always possible
        if n == 0:
            return True

        # Only zero can be placed on zero
        if len(flowerbed) == 0:
            return n == 0

        # If there are 2 spots: there must be at most 1 flower
        # (be it existing or new)
        if len(flowerbed) <= 2:
            return flowerbed.count(1) + n <= 1

        # Finally with at least 3 spots,
        # we can run a check through the array
        if len(flowerbed) < 3 and flowerbed.count(1) > 0 and n > 0:
            return False

        planted = 0
        for pos in range(len(flowerbed)):

            # Find 0 0 0 (or 0 0 and edge)
            if (pos == 0 or flowerbed[pos - 1] == 0) and \
               flowerbed[pos] == 0 and \
               (pos == len(flowerbed) - 1 or flowerbed[pos + 1] == 0):
                
                # Modify the flowerbed and count planted flowers
                flowerbed[pos] = 1
                planted += 1
            # Check if we have reached desirable number of planted flowers
            if planted == n:
                return True

        return False

def main():
    ''' Test canPlaceFlowers
    '''
    solution = Solution()

    test_cases = [
        ([1,0,0,0,1], 1),
        ([1,0,0,0,1], 2),
        ([], 0),
        ([], 1),
        ([0], 0),
        ([0], 1),
        ([1], 0),
        ([1], 1),
        ([0, 0], 1),
        ([1, 0], 1),
        ([1, 0], 2),
        ([1, 0, 0], 1),
        ([1, 0, 0], 2),
        ([1, 0, 1], 1),
        ([1, 0, 1], 0),
        ([0,0,0,0,0,1,0,0], 0),
        ([0,0,0,0,0,1,0,0], 1),
        ([0,0,0,0,0,1,0,0], 2),
        ([0,0,0,0,0,1,0,0], 3),
        ([0,0,0,0,0,1,0,0], 4),
        ([0,0,0,0,0,1,0,0], 5),
        ([0,0,0,0,0,1,0,0], 6),
        
    ]
    for flowerbed, n in test_cases:
        print(f"IN: {flowerbed}, {n}")
        result = solution.canPlaceFlowers(flowerbed, n)
        print(f"OUT: {flowerbed}, {result}\n")

if __name__ == "__main__":
    main()