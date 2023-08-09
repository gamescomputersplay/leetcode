''' https://leetcode.com/problems/combination-sum-ii/
'''

# This is a modification of the 0039
# Modifications marked in comments

class Solution:

    def combinationSum2(self, candidates, target):

        def combination_rec(target, start_from):

            if (target, start_from) in cache:
                return cache[(target, start_from)]

            all_options = set()

            # Continue the recursion
            for position, element in enumerate(candidates[start_from:], start=start_from):

                # How can we get remaining value from remaining elements
                new_target = target-element

                if new_target < 0:
                    continue

                if new_target == 0:
                    all_options.add((element,))
                else:
                    this_element_options = combination_rec(target-element, position + 1)
                    # Combine it with all next options
                    for option in this_element_options:
                        if option is not None:
                            all_options.add(tuple([element] + list(option)))

            cache[(target, start_from)] = all_options
            return all_options

        # Sort the candidates
        candidates.sort(reverse=True)

        # Filter excessive candidates:
        # don't include those that overshoot the target
        cand_filtered = []
        curr_number = candidates[0] - 1
        curr_count = 0
        for cand in candidates:
            if cand != curr_number:
                curr_number = cand
                curr_count = 1
            else:
                curr_count += 1
            if curr_number * curr_count <= target:
                cand_filtered.append(cand)
        candidates = cand_filtered

        # Keep track of combinations we looked at
        cache = {}

        # Start the recursion
        result = combination_rec(target, 0)

        return list(result)


def main():
    ''' Test combinationSum
    '''
    solution = Solution()

    test_cases = [
        ([10,1,2,7,6,1,5], 8),
        ([2,5,2,1,2], 5),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27),
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
