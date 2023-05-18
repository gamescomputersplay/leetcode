''' https://leetcode.com/problems/add-binary/
'''

class Solution:
    def addBinary(self, a, b):

        digits = []
        carry = 0
        digit_to_string = ["0", "1"]
        len_a, len_b = len(a), len(b)

        for p in range(max(len_a, len_b)):
            digit = carry + \
                (1 if len_a > p and a[-p-1] == "1" else 0) + \
                (1 if len_b > p and b[-p-1] == "1" else 0)
            carry = digit // 2
            digits.append(digit_to_string[digit % 2])
            
        if carry == 1:
            digits.append("1")

        return "".join(digits[::-1])
    
def main(verbose=True):
    ''' Test addBinary
    '''
    solution = Solution()

    test_cases = [
       ("11", "1"),
       ("1010", "1011"),
       ("111", "111"),
       ("0", "0"),
       ("0", "1"),
       ("1", "1"),
    ]

    for a, b in test_cases:
        result = solution.addBinary(a, b)
        if verbose:
            print(f"{a}, {b}: {result}")

def test_timing(runs=100):
    solution = Solution()
    a, b = "101"*3400, "1011"*2500
    start = time.time()
    for _ in range(runs):
        solution.addBinary(a, b)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    test_timing()