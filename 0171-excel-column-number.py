''' https://leetcode.com/problems/excel-sheet-column-number/
'''

class Solution:
    def titleToNumber(self, columnTitle):

        values = {ch: i + 1 for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

        result = 0
        for p, ch in enumerate(columnTitle[::-1]):
            result += values[ch] * 26 ** p
        return result

def main():
    ''' Test titleToNumber
    '''
    solution = Solution()

    test_cases = [
        "A", #1 
        "B", #2
        "Z", #26
        "AA", #27
        "AB", #27
        "ZY", #701
        "FXSHRXW", 

    ]
    for columnTitle in test_cases:
        result = solution.titleToNumber(columnTitle)
        print(columnTitle, result)

if __name__ == "__main__":
    main()

        