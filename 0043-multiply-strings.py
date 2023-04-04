''' https://leetcode.com/problems/multiply-strings/
'''

class Solution:
    def multiply(self, num1, num2):
        # Conversion table
        str2num = {str(n):n for n in range(10)}
        num2str = {n:str(n) for n in range(10)}

        # List to store sums if individual products
        by_digit = [0 for _ in range(len(num1) + len(num2))]
        for pos1, char1 in enumerate(num1[::-1]):
            for pos2, char2 in enumerate(num2[::-1]):
                by_digit[pos1 + pos2] += str2num[char1] * str2num[char2]

        # Calculate product as a string
        string = []
        carry = 0
        for digit in by_digit:
            digit += carry
            carry = digit // 10
            digit %= 10
            string.append(num2str[digit])

        # Trim zeros from that string
        while len(string) > 1 and string[-1] == "0":
            del string[-1]

        # Join the resulting string
        return "".join(string[::-1])

def main():
    ''' Test multiply
    '''
    solution = Solution()

    test_cases = [
        ("2", "3"),
        ("123", "456"),
        ("0", "2"),
        ("9999", "999999")
    ]
    for n1, n2 in test_cases:
        result = solution.multiply(n1, n2)
        is_correct = result == str(int(n1) * int(n2))
        print(n1, n2, result, is_correct)

if __name__ == "__main__":
    main()
