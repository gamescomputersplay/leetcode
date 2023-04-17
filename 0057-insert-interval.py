''' https://leetcode.com/problems/insert-interval/
'''

class Solution:
    def insert(self, intervals, newInterval):

        if not intervals:
            return [newInterval]

        resulting_intervals = []
        
        insert_start, insert_end = newInterval
        inserting_done = False

        for n, (start, end) in enumerate(intervals):

            save_current_interval = True

            # Find an overlap, merge current interval and inserted one
            if start <= insert_start <= end or start <= insert_end <= end:
                insert_start = min(insert_start, start)
                insert_end = max(insert_end, end)
                save_current_interval = False

            # Ignore intervals that are encircled by the inserted interval
            if start >= insert_start and end <= insert_end:
                save_current_interval = False


            # Write out inserted interval
            if not inserting_done and insert_end < start:
                resulting_intervals.append([insert_start, insert_end])
                inserting_done = True

            if save_current_interval:
                resulting_intervals.append([start, end])

            # Also do it if it is the last interval
            if not inserting_done and insert_end >= start and n == len(intervals) - 1:
                resulting_intervals.append([insert_start, insert_end])


        return resulting_intervals

def main():
    ''' Test insert
    '''
    solution = Solution()

    test_cases = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,3],[6,9]], [7, 100]),
        ([[2,3],[4, 5], [10, 11]], [3, 4]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
        ([], [5,7]),
        ([[5, 6]], [5,7]),
        ([[1, 5]], [6, 8]),
        ([[2,5],[6,7],[8,9]], [0,1]),
    ]
    for intervals, newInterval in test_cases:
        result = solution.insert(intervals, newInterval)
        print(intervals, newInterval, "\n", result, "\n")

if __name__ == "__main__":
    main()