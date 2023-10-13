''' https://leetcode.com/problems/compare-version-numbers/
'''

class Solution:
    def compareVersion(self, version1, version2):

        # Parce version number into chunks
        parsed = []
        # Keep track of longest version
        verlen = 0
        for version in [version1, version2]:
            parsed.append([])
            for chunk in version.split("."):
                parsed[-1].append(int(chunk))
            verlen = max(verlen, len(parsed[-1]))

        # Pad shorted version with zeros
        for version in parsed:
            while len(version) < verlen:
                version.append(0)

        # Compare
        for v1, v2 in zip(parsed[0], parsed[1]):
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1

        return 0

def main():
    ''' Test compareVersion
    '''
    solution = Solution()

    test_cases = [
        ("1.01", "1.001"),
        ("1.0", "1.0.0"),
        ("0.1", "1.1"),
        ("1", "2"),
        ("1", "2.3.4.5.6")
    ]
    for version1, version2 in test_cases:
        result = solution.compareVersion(version1, version2)
        print(version1, version2, result)

if __name__ == "__main__":
    main()
        