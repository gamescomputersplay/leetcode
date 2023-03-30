''' https://leetcode.com/problems/combination-sum/
'''

class Solution:

    def __init__(self):
        self.cache = {}

    def combinationSum_recursive(self, candidates, target):

        cache_index = tuple(candidates + [target])

        if cache_index in self.cache:
            return self.cache[cache_index]

        if target == 0:
            self.cache[cache_index] = [[]]
            return [[]]

        out = set()
        
        for candidate in candidates:

            new_target = target - candidate

            if new_target >= 0:
                results = self.combinationSum_recursive(candidates, new_target)

                for result in results:
                    sorted_result = [candidate] + list(result)
                    sorted_result.sort()
                    out.add(tuple(sorted_result))

        #out = [list(item) for item in out]
        self.cache[cache_index] = out
        return out

    def combinationSum(self, candidates, target):

        result = self.combinationSum_recursive(candidates, target)
        out = [list(item) for item in result]
        return out

def main():
    ''' Test combinationSum
    '''
    solution = Solution()

    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]
    for candidates, target in test_cases:
        print(candidates, target, solution.combinationSum(candidates, target))

def large_case():
    solution = Solution()

    candidates = [n for n in range(2, 41)]
    target = 59
    start = time.time()
    result = solution.combinationSum(candidates, target)
    elapsed = time.time() - start
    print(f"{len(result)} solution in {elapsed} s")


if __name__ == "__main__":
    import time
    main()
    large_case()
