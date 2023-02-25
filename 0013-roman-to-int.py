''' https://leetcode.com/problems/roman-to-integer/
'''
class Solution:
    def romanToInt(self, s):

        # Simple mapping
        romans_map = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
            }

        result = 0
        previous = 0

        for letter in s:

            current_value = romans_map[letter]

            # This one catches IV,IX adn so on
            if current_value > previous:
                result -= previous * 2

            result += current_value
            previous = current_value

        return result

def main():
    ''' Test intToRoman
    '''
    solution = Solution()

    test_cases = [
        ('III', 3),
        ('LVIII', 58),    
        ('MCMXCIV', 1994),
        ('I', 1),
        ('CCLXXII', 272), 
        ('DXLIII', 543),  
        ('DCCCXIV', 814), 
        ('MLXXXV', 1085),
        ('MCCCLVI', 1356),
        ('MDCXXVII', 1627),
        ('MDCCCXCVIII', 1898),
        ('MMCLXIX', 2169),
        ('MMCDXL', 2440),
        ('MMDCCXI', 2711),
        ('MMCMLXXXII', 2982),
        ('MMMCCLIII', 3253),
        ('MMMDXXIV', 3524),
        ('MMMDCCXCV', 3795),
    ]
    for roman, arabic in test_cases:
        result = solution.romanToInt(roman)
        print(roman, result, result == arabic)


if __name__ == "__main__":
    main()
