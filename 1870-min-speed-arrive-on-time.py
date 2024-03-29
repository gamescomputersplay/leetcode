''' https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
'''

import math

class Solution:
    def minSpeedOnTime(self, dist, hour):

        def find_fist_more_than_num(arr, num):

            if arr==[]:
                return 0

            if arr[-1] < num:
                return len(arr)
            
            if arr[0] >= num:
                return 0

            left = 0
            right = len(arr)
            while True:
                center = (left + right) // 2

                if arr[center] >= num > arr[center-1] or center == 0:
                    return center
                if arr[center] >= num:
                    right = center
                else:
                    left = center

        def doable(speed):
            ''' Whether teh task is doable of teh speed is "speed"
            '''
            nonlocal cache
            if speed in cache:
                return cache[speed]
            
            one_hours = find_fist_more_than_num(dist[:-1], speed)
            used_time = one_hours

            for s in dist[one_hours:-1]:
                if speed > s:
                    used_time += 1
                else:
                    used_time += math.ceil(s / speed)
            used_time += dist[-1] / speed
            cache[speed] = used_time <= hour
            return cache[speed]

        # Impossible since each one but one takes at least an hour
        if len(dist) - 1 >= hour:
            return -1

        if sum(dist) <= hour:
            return 1

        left = 1
        right = sum(dist) + 1

        # When we need to try to squeeze last one into 1 hour
        if hour != int(hour):
            right = max(right, int(dist[-1]/(hour-int(hour)))+2)

        cache = {}
        dist = sorted(dist[:-1]) + [dist[-1]]

        while True:
            center = (left + right) // 2

            if doable(center) and not doable(center - 1):
                return center
            if doable(center):
                right = center
            else:
                left = center

def random_test(runs=100):

    def doable(speed, dist, hour):
        ''' Whether teh task is doable of teh speed is "speed"
        '''
        used_time = 0
        for s in dist[:-1]:
            used_time += math.ceil(s / speed)
        used_time += dist[-1] / speed
        return used_time <= hour

    solution = Solution()
    for _ in range(runs):
        dist = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        hour = random.random() * 20 + 1
        #print(dist, hour)
        result = solution.minSpeedOnTime(dist, hour)
        if result != -1:
            if not doable(result, dist, hour) or result > 1 and doable(result-1, dist, hour):
                print(f"Error at: {dist}, {hour}")
                return
    print(f"{runs} tests okay")

def large_case(size=1000):
    solution = Solution()
    dist = [x for x in range(1, size)]
    hour = size*2
    start = time.time()
    solution.minSpeedOnTime(dist, hour)
    elapsed = time.time() - start
    print(f"Large case: {elapsed}s")

def main():
    ''' Test minSpeedOnTime
    '''
    solution = Solution()

    test_cases = [
        ([1,3,2], 6),
        ([1,3,2], 2.7),
        ([1,3,2], 1.9),
        ([1], 2),
        ([8, 1, 1, 7], 3.03),
    ]
    for dist, hour in test_cases:
        result = solution.minSpeedOnTime(dist, hour)
        print(dist, hour, result)

if __name__ == "__main__":
    import random
    import time
    main()
    random_test(10000)
    large_case(1_000_000)
