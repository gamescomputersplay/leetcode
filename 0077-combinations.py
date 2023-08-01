''' https://leetcode.com/problems/combinations/
'''

import math
class Solution:
    def combine(self, n, k):

        # Fist combination is [1, 2, 3, ...]
        combs = [[i for i in range(1, k + 1)]]

        # This is how many more combinations we need to add
        comb_count = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

        for _ in range(comb_count - 1):
            # Start with the previous combination
            comb = combs[-1].copy()

            # Find first position from the right, that can be increased by 1
            # In such a way that all position to the right of it, are +1, +1, +1
            for pos_back in range(k-1, -1, -1):
                if comb[pos_back] < n + pos_back + 1 - k:
                    comb[pos_back] += 1
                    for pos_forward in range(pos_back + 1, k):
                        comb[pos_forward] = comb[pos_forward - 1] + 1 
                    break

            combs.append(comb)

        return combs

    def combine_prev(self, n, k):

        # Start with [[1], [2], [3],...]
        combs = [[i] for i in range(1, n + 1)]

        # Then add numbers uup to k
        for _ in range(k - 1):

            new_combs = []

            # Take whatever you have so far
            for comb in combs:

                # And add all numbers larger than the last one
                for i in range(comb[-1] + 1, n + 1):
                    new_combs.append(comb + [i])

            combs = new_combs

        return combs


def main():
    ''' Test combine
    '''
    solution = Solution()

    test_cases = [
        [5, 3],
        [4, 2],
        [1, 1],
    ]

    for n ,k in test_cases:
        result = solution.combine(n ,k)
        print(n ,k, result, len(result), "\n")

def time_test():
    solution = Solution()
    start = time.time()
    for _ in range(1):
        result = solution.combine(20, 10)
    elapsed = time.time() - start
    print(len(result), elapsed)

if __name__ == "__main__":
    import time
    main()
    time_test()
