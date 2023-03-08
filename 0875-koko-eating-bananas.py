''' https://leetcode.com/problems/koko-eating-bananas/
'''

class Solution:

    def __init__(self):
        # Cache results of testing if these days are acceptable
        self.cache = {}

    def can_eat(self, piles, h, speed):
        ''' Can Koko eat bananas in time with this speed, False or True
        '''
        # Use cache if answer is there
        if speed in self.cache:
            return self.cache[speed]
        elapsed_time = 0
        for pile in piles:
            # Simple substitute for "Ceiling"
            elapsed_time += (pile + speed - 1) // speed
            if elapsed_time > h:
                self.cache[speed] = False
                return False
        self.cache[speed] = True
        return True


    def minEatingSpeed(self, piles, h):
        # Flush the cache
        self.cache = {}

        piles.sort(reverse=True)
        # Borders for binary search
        slowest = 1
        fastest = max(piles) + 1

        #Binary search
        while True:
            middle_speed = (slowest + fastest) // 2

            # Success if when this number of day is okay, but "this - 1" is not
            if self.can_eat(piles, h, middle_speed) and \
                (middle_speed == 1 or \
                not self.can_eat(piles, h, middle_speed-1)):
                return middle_speed
            
            # Whether the current guess is okay time will determine which 
            # half of search space to keep
            if self.can_eat(piles, h, middle_speed):
                fastest = middle_speed
            else:
                slowest = middle_speed


    def minEatingSpeedBrute(self, piles, h):
        ''' Same with brute force
        '''
        # Flush the cache
        self.cache = {}

        test_speed = 1
        while True:
            if self.can_eat(piles, h, test_speed):
                return test_speed
            test_speed += 1


def test_manual():
    ''' Test minimumTime
    '''
    solution = Solution()

    test_cases = [
        ([3, 6, 7, 11], 8), # 4
        ([30, 11, 23, 4, 20], 5), # 30
        ([1], 1), # 1
        ([2], 1), # 2
        ([1], 2), # 1
        ([1, 10], 2), # 10
        ([1, 10], 10), # 5
        ([1], 10), # 1
        ([10], 1), # 10
            ]
    for piles, hours in test_cases:
        result1 = solution.minEatingSpeedBrute(piles, hours)
        result2 = solution.minEatingSpeed(piles, hours)
        print(piles, hours, result1, result2, result1 == result2)
        if result1 != result2:
            print("Error")
            print(piles, hours)
            break

def random_test(runs):
    ''' Run "runs" randomly generated tests
    '''
    solution = Solution()
    for _ in range(runs):
        piles = [random.randint(1, 10) for _ in range(random.randint(1, 100))]
        hours = random.randint(len(piles), 100)
        result1 = solution.minEatingSpeedBrute(piles, hours)
        result2 = solution.minEatingSpeed(piles, hours)
        #print(buses_times, target_trips, result1, result2, result1 == result2)
        if result1 != result2:
            print("Error")
            print(piles, hours)
            return
    print(f"{runs} tests, all ok")

def timing_run(max_power, func):
    ''' See how well it performs against brute
    '''
    for power in range(0, max_power + 1):
        size = 2 ** power

        piles = [random.randint(1, size) for i in range(size)]

        start = time.time()
        for _ in range(100):
            hours = random.randint(len(piles), size)
            func(piles, hours)
        elapsed = time.time() - start

        print(f"Power: {power}, Size: {size}, Time: {elapsed}")

def timing_test():
    random.seed(0)
    solution = Solution()
    timing_run(10, solution.minEatingSpeedBrute)
    print()
    timing_run(13, solution.minEatingSpeed)

if __name__ == "__main__":
    import random
    import time
    test_manual()
    random_test(10000)
    timing_test()