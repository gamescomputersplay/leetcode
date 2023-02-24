''' https://leetcode.com/problems/integer-to-roman/
'''

class Solution:
    def intToRoman(self, num):
        
        # Conversion data
        romans_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
            }

        # Will append roman letter to this string
        result = ""

        # Make sure the map is sorted from largest to smallest
        for value, roman in sorted(romans_map.items(), reverse=True):

            # Add a letter as long as there is enough value left
            while num >= value:
                num -= value
                result += roman
        
        return result

def main():
    ''' Test intToRoman
    '''
    solution = Solution()

    test_cases = [3, 58, 1994] + \
    [
        i for i in range(1, 4000, 371)
    ]
    for num in test_cases:
        result = solution.intToRoman(num)
        print(num, result)



if __name__ == "__main__":
    main()
