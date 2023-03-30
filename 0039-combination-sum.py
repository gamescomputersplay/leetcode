''' https://leetcode.com/problems/combination-sum/
'''

class Solution:

    def __init__(self):
        self.cache = {}

    def combinationSum(self, candidates, target):

        cache_index = tuple(candidates + [target])

        if cache_index in self.cache:
            return self.cache[cache_index]

        if target == 0:
            self.cache[cache_index] = [[]]
            return [[]]
        
        if target < 0:
            self.cache[cache_index] = []
            return []

        out = set()
        
        for candidate in candidates:

            new_candidates = candidates.copy()
            new_target = target - candidate

            results = self.combinationSum(new_candidates, new_target)

            for result in results:
                sorted_result = [candidate] + result
                sorted_result.sort()
                out.add(tuple(sorted_result))

        out = [list(item) for item in out]
        self.cache[cache_index] = out
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

if __name__ == "__main__":
    main()
