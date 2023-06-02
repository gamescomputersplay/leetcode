''' https://leetcode.com/problems/combinations/
'''

class Solution:
        

    def combine(self, n, k):

        def add_element(sofar):

            if sofar in done:
                return
            done.add(sofar)

            if len(sofar) == k:
                result.add(sofar)
                return

            for i in range(1, n + 1):
                if i in sofar:
                    continue
                new_sofar = tuple(sorted(sofar + (i,)))
                add_element(new_sofar)

        result = set()
        done = set()

        add_element(())
        return [list(element) for element in result]

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
