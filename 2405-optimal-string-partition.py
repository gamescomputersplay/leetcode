''' https://leetcode.com/problems/optimal-partition-of-string/
'''

class Solution:
    def partitionString(self, s):

        chars_so_far = set()
        partition_counter = 1

        for char in s:

            if char in chars_so_far:
                chars_so_far = set(char)
                partition_counter += 1

            else:
                chars_so_far.add(char)

        return partition_counter

def main():
    ''' Test partitionString
    '''
    solution = Solution()

    test_cases = [
        "abacaba",
        "ssssss",
        "a",

    ]
    for string in test_cases:

        result = solution.partitionString(string)
        print(string, result)


if __name__ == "__main__":
    main()
