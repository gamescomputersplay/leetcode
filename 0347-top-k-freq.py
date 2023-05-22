''' https://leetcode.com/problems/top-k-frequent-elements/
'''

class Solution:
    def topKFrequent(self, nums, k):

        # Make a dict with all frequencies
        freqs_dict = {}
        for num in nums:
            freqs_dict[num] = freqs_dict.get(num, 0) + 1

        # Convert it into list and sort by negative frequency
        freqs_list = list(freqs_dict.items())
        freqs_list.sort(key=lambda x: -x[1])

        # Get the values and cut to k
        return [freq[0] for freq in freqs_list[:k]]

def main():
    ''' Test topKFrequent
    '''
    solution = Solution()

    test_cases = [
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([1], 0),
    ]

    for nums, k in test_cases:
        result = solution.topKFrequent(nums, k)
        print(nums, k, result)

if __name__ == "__main__":
    import time
    main()
