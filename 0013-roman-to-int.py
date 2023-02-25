''' https://leetcode.com/problems/roman-to-integer/
'''
class Solution:
    def romanToInt(self, s):
        return 0

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
