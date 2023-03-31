''' https://leetcode.com/problems/combination-sum-ii/
'''

# This is a modification of the 0039
# Modifications marked in comments

class Solution:

    def __init__(self):
        self.cache = {}

    def combination_rec(self, candidates, target, start):

        if (target, start) in self.cache:
            return self.cache[(target, start)]

        if target == 0:
            self.cache[(target, start)] = [[]]
            return [[]]

        out = set()

        for new_start in range(start, len(candidates)):

            candidate = candidates[new_start]
            new_target = target - candidate

            if new_target >= 0:
                results = self.combination_rec(candidates, new_target, new_start + 1)
                for result in results:
                    out.add(tuple([candidate] + list(result)))
                    
        self.cache[(target, start)] = out
        return out

    def combinationSum2(self, candidates, target):

        # Sort the candidates
        candidates.sort(reverse=False)

        start = 0
        out = self.combination_rec(candidates, target, start)
        # Convert to lists
        out = [list(item) for item in out]
        return out

    #### Below is the old solution

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

    def combinationSum2_old(self, candidates, target):

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
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27)
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
