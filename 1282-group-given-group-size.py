''' https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
'''

class Solution:
    def groupThePeople(self, groupSizes):

        # {size: [groups of this size]}
        groups = {}

        for n, groupSize in enumerate(groupSizes):

            # Create key for the new size
            if groupSize not in groups:
                groups[groupSize] = [[]]
            # Create new list if previous filled up
            if len(groups[groupSize][-1]) == groupSize:
                groups[groupSize].append([])
            # Ad percon to the list
            groups[groupSize][-1].append(n)
        
        # Transform dict into list
        result = []
        for group in groups.values():
            result.extend(group)
        return result

def main():
    ''' Test groupThePeople
    '''
    solution = Solution()

    test_cases = [
        [3,3,3,3,3,1,3],
        [2,1,3,3,3,2],
        [1],
    ]
    for groupSizes in test_cases:
        result = solution.groupThePeople(groupSizes)
        print(groupSizes, result)


if __name__ == "__main__":
    main()
        