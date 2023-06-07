''' https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
'''

class Solution:
    def minFlips(self, a, b, c):
        count = 0
        while a > 0 or b > 0 or c > 0:

            # 0 requires both 0s
            if c % 2 == 0:
                count += (1 if a % 2 == 1 else 0)
                count += (1 if b % 2 == 1 else 0)
            # 1 resuires at least one 1
            else:
                if a % 2 == 0 and b % 2 == 0:
                    count += 1

            a //= 2
            b //= 2
            c //= 2

        return count

def main():
    ''' Test minFlips
    '''
    solution = Solution()

    test_cases = [
        (2, 6, 5),
        (4, 2, 7),
        (1, 2, 3),
        (1, 10, 255),
        (5, 2, 8)
    ]
    for a, b, c in test_cases:
        result = solution.minFlips(a, b, c)
        print(a, b, c, result)


if __name__ == "__main__":
    main()
