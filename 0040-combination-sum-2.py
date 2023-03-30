''' https://leetcode.com/problems/combination-sum-ii/
'''

# This is a modification of the 0039
# Modifications marked in comments

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

            # These two are new lines
            new_candidates = candidates.copy()
            new_candidates.remove(candidate)

            new_target = target - candidate

            if new_target >= 0:
                # new_candidates is new
                results = self.combinationSum_recursive(new_candidates, new_target)

                for result in results:
                    sorted_result = [candidate] + list(result)
                    sorted_result.sort()
                    out.add(tuple(sorted_result))

        self.cache[cache_index] = out
        return out

    def combinationSum2(self, candidates, target):

        result = self.combinationSum_recursive(candidates, target)
        out = [list(item) for item in result]
        return out

def main():
    ''' Test combinationSum
    '''
    solution = Solution()

    test_cases = [
        ([10,1,2,7,6,1,5], 8),
        ([2,5,2,1,2], 5),
    ]
    for candidates, target in test_cases:
        print(candidates, target, solution.combinationSum2(candidates, target))

def large_case():
    solution = Solution()

    candidates = [n for n in range(2, 41)]
    target = 59
    start = time.time()
    result = solution.combinationSum2(candidates, target)
    elapsed = time.time() - start
    print(f"{len(result)} solution in {elapsed} s")


if __name__ == "__main__":
    import time
    main()
    large_case()
