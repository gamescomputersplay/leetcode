''' https://leetcode.com/problems/group-anagrams/
'''

class Solution:

    def groupAnagrams(self, strs):

        # Dict to categorize strs
        groups = {}

        for str in strs:

            # ID is tuple (immutable) and sorted (same for anagrams)
            group_id = tuple(sorted(str))

            # Store results in lists
            if group_id not in groups:
                groups[group_id] = []
            groups[group_id].append(str)

        return list(groups.values())

def main():
    ''' Test groupAnagrams
    '''
    solution = Solution()

    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]
    for strs in test_cases:
        result = solution.groupAnagrams(strs)
        print(strs, result)

if __name__ == "__main__":
    main()
