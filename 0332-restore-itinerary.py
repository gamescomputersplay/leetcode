''' https://leetcode.com/problems/reconstruct-itinerary/
'''

class Solution:
    def findItinerary(self, tickets):

        def try_next(visited):
            nonlocal answer

            if answer is not None:
                return None

            # Answer is found, pool is empty
            if not pool and answer is None:
                answer = visited

            we_are_at = visited[-1]
            if we_are_at not in pool:
                return None

            for next_stop in sorted(pool[we_are_at].keys()):

                new_visited = visited.copy()
                new_visited.append(next_stop)

                # New pool, remove ticket and adjust
                pool[we_are_at][next_stop] -= 1
                if pool[we_are_at][next_stop] == 0:
                    del pool[we_are_at][next_stop]
                if len(pool[we_are_at]) == 0:
                    del pool[we_are_at]

                try_next(new_visited)

                if we_are_at not in pool:
                    pool[we_are_at] = {}
                if next_stop not in pool[we_are_at]:
                    pool[we_are_at][next_stop] = 0
                pool[we_are_at][next_stop] += 1


        # Pool of tickets with counts:
        # {from1: {to1: 1, to2:2,...}, ...}
        pool = {}
        for frm, to in tickets:
            if frm not in pool:
                pool[frm] = {}
            if to not in pool[frm]:
                pool[frm][to] = 0
            pool[frm][to] += 1

        answer = None
        try_next(["JFK",])

        return answer

def main():
    ''' Test findItinerary
    '''
    solution = Solution()

    test_cases = [
        [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
        [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
        [],
        [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]],
    ]

    for tickets in test_cases:
        print()
        result = solution.findItinerary(tickets)
        print(len(tickets), tickets, result)

if __name__ == "__main__":
    main()
