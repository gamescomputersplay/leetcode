''' https://leetcode.com/problems/minimum-time-to-complete-trips/
'''

class Solution:

    def __init__(self):
        # Cache results of testing if these days are acceptable
        self.cache = {}

    def is_doable_in_this_limit(self, time, totalTrips, time_to_test):
        ''' Is it possible to complete the task
        within time_to_test amount of time
        '''
        # Use cache if answer is there
        if time_to_test in self.cache:
            return self.cache[time_to_test]

        trips_so_far = 0
        for one_bus_time in time:
            trips_so_far += time_to_test // one_bus_time
            if trips_so_far >= totalTrips:
                self.cache[time_to_test] = True
                return True
        self.cache[time_to_test] = False
        return False

    def minimumTime(self, time, totalTrips):
        # Flush the cache
        self.cache = {}
        # Put more efficient buses in front, it will help calculate successful days faster
        time.sort()

        # Borders for binary search
        shortest_time = 1
        longest_time = totalTrips * max(time) + 1

        #Binary search
        while True:
            middle_time = (shortest_time + longest_time) // 2

            # Success if when this number of day is okay, but "this - 1" is not
            if self.is_doable_in_this_limit(time, totalTrips, middle_time) and \
                (middle_time == 1 or \
                not self.is_doable_in_this_limit(time, totalTrips, middle_time-1)):
                return middle_time
            
            # Whether the current guess is okay time will determine which 
            # half of search space to keep
            if self.is_doable_in_this_limit(time, totalTrips, middle_time):
                longest_time = middle_time
            else:
                shortest_time = middle_time



    def minimumTimeBrute(self, time, totalTrips):
        ''' Same but brute force
        '''
        # Flush the cache
        self.cache = {}
        # Start with 1, and go one by one
        time_to_test = 1
        while True:
            if self.is_doable_in_this_limit(time, totalTrips, time_to_test):
                return time_to_test
            time_to_test +=1


def test_manual():
    ''' Test minimumTime
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3], 5), # 3
        ([1, 2, 3, 4], 5), # 3
        ([1], 1), # 1
        ([2], 1), # 2
        ([1], 2), # 2
        ([1, 10], 1), # 1
        ([1, 10], 10), # 10
        ([1], 10), # 10
        ([10], 1), # 10
    ]
    for buses_times, target_trips in test_cases:
        result1 = solution.minimumTimeBrute(buses_times, target_trips)
        result2 = solution.minimumTime(buses_times, target_trips)
        print(buses_times, target_trips, result1, result2, result1 == result2)
        if result1 != result2:
            print("Error")
            print(buses_times, target_trips)
            break

def random_test(runs):
    ''' Run "runs" randomly generated tests
    '''
    solution = Solution()
    for _ in range(runs):
        buses_times = [random.randint(1, 10) for _ in range(100)]
        target_trips = random.randint(1, 100)
        result1 = solution.minimumTimeBrute(buses_times, target_trips)
        result2 = solution.minimumTime(buses_times, target_trips)
        #print(buses_times, target_trips, result1, result2, result1 == result2)
        if result1 != result2:
            print("Error")
            print(buses_times, target_trips)
            return
    print(f"{runs} tests, all ok")

def timing_run(max_power, func):
    ''' See how well it performs against brute
    '''
    for power in range(0, max_power + 1):
        size = 2 ** power

        buses_times = [random.randint(1, size) for i in range(size)]

        start = time.time()
        for _ in range(100):
            target_trips = random.randint(1, size)
            func(buses_times, target_trips)
        elapsed = time.time() - start

        print(f"Power: {power}, Size: {size}, Time: {elapsed}")

def timing_test():
    random.seed(0)
    solution = Solution()
    #timing_run(13, solution.minimumTimeBrute)
    #print()
    timing_run(13, solution.minimumTime)

if __name__ == "__main__":
    import random
    import time
    test_manual()
    random_test(10000)
    timing_test()