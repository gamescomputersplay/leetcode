''' https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''

class Solution:
    def is_shipping_possible(self, weights, capacity, days):
        ''' Is it possible to do the shipping with this
        capacity, in that many days
        '''
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
                    return True

        return False

    def shipWithinDays(self, weights, days):
        
        return -1

    def shipWithinDaysBrute(self, weights, days):
        ''' Same, but by 1 increments
        '''
        capacity = max(max(weights), sum(weights)//days)

        while True:
            if self.is_shipping_possible(weights, capacity, days):
                return capacity
            capacity += 1



def main():
    ''' Test shipWithinDays
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5), #15
        ([3,2,2,4,1,4], 3), #6
        ([1,2,3,1,1], 4), #3
    ]
    for weights, days in test_cases:
        result = solution.shipWithinDaysBrute(weights, days)
        print(weights, days, result)

if __name__ == "__main__":
    main()
