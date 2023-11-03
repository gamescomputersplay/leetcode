''' https://leetcode.com/problems/build-an-array-with-stack-operations/
'''

class Solution:
    def buildArray(self, target, n):

        operatinos = []

        current = 1
        for num in target:
            # Push-pop until the next element is ready
            while current != num:
                operatinos.append("Push")
                operatinos.append("Pop")
                current += 1
            # Push and NOT pop
            operatinos.append("Push")
            current += 1

        return operatinos

def main():
    ''' Test buildArray
    '''
    solution = Solution()

    test_cases = [
        ([1,3], 3),
        ([1,2,3], 3),
        ([1], 10)
    ]
    for target, n in test_cases:
        result = solution.buildArray(target, n)
        print(target, n, result)

if __name__ == "__main__":
    main()
