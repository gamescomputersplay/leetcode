''' https://leetcode.com/problems/count-and-say/
'''

class Solution:
    def countAndSay(self, n):

        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)

        result = ""
        prev = None
        count = 0

        for char in s:

            if prev is not None and char != prev:
                result += str(count) + prev
                count = 0

            prev = char
            count += 1

        result += str(count) + s[-1]

        return result

def main():
    ''' Test countAndSay
    '''
    solution = Solution()

    for n in range(1, 15):
        print(f"{n}: {solution.countAndSay(n)}")

if __name__ == "__main__":
    main()