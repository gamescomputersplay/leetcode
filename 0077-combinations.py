''' https://leetcode.com/problems/combinations/
'''

class Solution:
    def combine(self, n, k):

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
