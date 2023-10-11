''' https://leetcode.com/problems/number-of-flowers-in-full-bloom/
'''

class Solution:
    def fullBloomFlowers(self, flowers, people):

        # Points at which number of F change
        diffs = {}
        for f_start, f_end in flowers:
            diffs[f_start] = diffs.get(f_start, 0) + 1
            diffs[f_end + 1] = diffs.get(f_end + 1, 0) - 1

        # Number of F on the day (and next days until it changes)
        daily = [(0, 0)]
        for day in sorted(diffs.keys()):
            daily.append((day, daily[-1][1] + diffs[day]))
        # Add end of times for simpler 2-pointer
        daily.append((float("inf"), 0))

        # 2-pointer through these two lists, finding person:result
        p_day = 0
        result_per_person = {}
        for person in sorted(people):

            while daily[p_day][0] <= person:
                p_day += 1
            result_per_person[person] = daily[p_day - 1][1]

        # Put results in the same order as people
        return [result_per_person[person] for person in people]

def main():
    ''' Test fullBloomFlowers
    '''
    solution = Solution()

    test_cases = [
        ([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11,6]),
        ([[1,10],[3,3]], [3,3,2]),
        ([], [1]),
    ]
    for flowers, people in test_cases:

        result = solution.fullBloomFlowers(flowers, people)
        print(flowers, people, result)


if __name__ == "__main__":
    main()
        