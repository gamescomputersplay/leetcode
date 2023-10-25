''' https://leetcode.com/problems/k-th-symbol-in-grammar/
'''

class Solution:
    def kthGrammar(self, n, k):

        k -= 1

        if n == 1:
            return 0

        power2 = 2 ** (n - 2)

        top = 0

        while power2 > 0:
            next = k // power2
            k = k - power2 * next
            top = (top + next) % 2

            power2 //= 2

        return top

def main():
    ''' Test kthGrammar
    '''
    solution = Solution()

    test_cases = [
        (1, 1),
        (2, 1),
        (2, 2),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4),
        (5, 10),
    ]
    for n, k in test_cases:
        result = solution.kthGrammar(n, k)
        print(f"{n}, {k}: {result}")

if __name__ == "__main__":
    main()
