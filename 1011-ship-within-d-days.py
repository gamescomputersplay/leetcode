''' https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''

class Solution:

    def __init__(self):
        self.cache = {}
        self.weights_sorted = None

    def is_shipping_possible(self, weights, capacity, days):
        ''' Is it possible to do the shipping with this
        capacity, in that many days
        '''
        if capacity in self.cache:
            return self.cache[capacity]

        pointer = 0

        # Simulate loading by going through all the days
        for _ in range(days):

            # Load is emptied at the beginning of each day
            daily_load = 0

            # And then we keep putting stuff on as long as there is room
            while daily_load + weights[pointer] <= capacity:
                daily_load += weights[pointer]

                # Moving along the conveyer as we do
                pointer += 1

                # If we used up all weights - task is doable
                if pointer == len(weights):
                    self.cache[capacity] = True
                    return True

        self.cache[capacity] = False
        return False

    def is_shipping_possible(self, weights, capacity, allowed_days):
        ''' Is it possible to do the shipping with this
        capacity, in that many days
        '''
        if capacity in self.cache:
            return self.cache[capacity]
        this_day = 0
        used_days = 1

        for weight in weights:

            if this_day + weight > capacity:
                used_days += 1
                this_day = weight
            if this_day + weight == capacity:
                used_days += 1
                this_day = 0
            else:
                this_day += weight
            if used_days > allowed_days:
                self.cache[capacity] = False
                return False
        self.cache[capacity] = True
        return True


    def shipWithinDays(self, weights, days):
        ''' Now let's do it with binary search
        '''
        # Flush the cache
        self.cache = {}
        self.weights_sorted = weights.copy()
        self.weights_sorted.sort(reverse=True)
        
        left = max(max(weights), sum(weights)//days)
        right = sum(weights)

        while True:
            middle = (left + right) // 2
            # print(left, middle, right, self.is_shipping_possible(weights, middle, days), self.is_shipping_possible(weights, middle-1, days))
            # Check if we found the sweet spot
            # Possible with this capacity, but not a smaller capacity
            if self.is_shipping_possible(weights, middle, days) and \
                not (middle == 1 or self.is_shipping_possible(weights, middle - 1, days)):
                break

            # If if was possible - this is new right (larger) bound
            if self.is_shipping_possible(weights, middle, days):
                right = middle
            # Else - left (smaller) bound
            else:
                left = middle

        return middle

    def shipWithinDaysBrute(self, weights, days):
        ''' Same, but by 1 increments
        '''
        self.cache = {}

        capacity = max(max(weights), sum(weights)//days)

        while True:
            if self.is_shipping_possible(weights, capacity, days):
                return capacity
            capacity += 1

def random_test(runs=10, maxlen=10):
    solution = Solution()
    for _ in range(runs):
        weights = [random.randint(1, 500) for i in range(maxlen)]
        days = random.randint(1, maxlen)
        result1 = solution.shipWithinDaysBrute(weights, days)
        result2 = solution.shipWithinDays(weights, days)
        if result1 != result2:
            print("Error")
            print(weights, days, result1, result2)
            break
    else:
        print(f"{runs} cases tested okay") 

def test_one_case():
    ''' Test shipWithinDays
    '''
    solution = Solution()

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    result1 = solution.shipWithinDaysBrute(weights, days)
    result2 = solution.shipWithinDays(weights, days)
    print(weights, days, result1, result2, result1 == result2)


def test_manual():
    ''' Test shipWithinDays
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5), # 15
        ([3,2,2,4,1,4], 3), # 6
        ([1,2,3,1,1], 4), # 3
        ([1,2,3,4,1], 1), # 11
        ([1,2,3,4,1], 11), # 
        ([10], 1), # 10 
        ([10], 10), # 10
    ]
    for weights, days in test_cases:
        result1 = solution.shipWithinDaysBrute(weights, days)
        result2 = solution.shipWithinDays(weights, days)
        print(weights, days, result1, result2, result1 == result2)
        if result1 != result2:
            print("Error")
            print(weights, days)
            break

def timing_run(max_power, func):
    ''' See how well it performs against brute
    '''
    for power in range(0, max_power + 1):
        size = 2 ** power

        weights = [random.randint(1, 500) for i in range(size)]
        start = time.time()
        for _ in range(100):
            days = random.randint(1, size)
            func(weights, days)
        elapsed = time.time() - start
        print(f"Power: {power}, Size: {size}, Time: {elapsed}")

def timing_test():
    solution = Solution()
    #timing_run(12, solution.shipWithinDaysBrute)
    print()
    timing_run(12, solution.shipWithinDays)

if __name__ == "__main__":
    import random
    import time
    test_one_case()
    #test_manual()
    #random_test(1000)
    #timing_test()
