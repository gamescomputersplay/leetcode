''' https://leetcode.com/problems/counting-bits/
'''

class Solution:
    def countBits(self, n):

        result = [0]
        if n == 0:
            return result

        chunk_size = 1

        while True:
            for i in range(chunk_size):
                result.append(result[- chunk_size + i] + 1)
                if len(result) == n + 1:
                    return result
            chunk_size *= 2

def main():
    ''' Test countBits
    '''
    solution = Solution()

    test_cases = [
        0, 1, 2, 5, 100
    ]

    for n in test_cases:
        result = solution.countBits(n)
        print(n, result)

if __name__ == "__main__":
    main()
