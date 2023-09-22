''' https://leetcode.com/problems/shortest-path-visiting-all-nodes/
'''

class Solution:
    def shortestPathLength(self, graph):

        def non_back_tracking_path(start):
            ''' Returns all non-backtracking paths from start
            '''
            stack = [[start]]
            while True:

                has_updates = False
                new_stack = []

                for so_far in stack:

                    for potential_next in graph[so_far[-1]]:
                        new_so_far = so_far.copy()
                        if potential_next not in so_far:
                            new_so_far.append(potential_next)
                            has_updates = True
                            new_stack.append(new_so_far)

                if not has_updates:
                    return stack
                stack = new_stack

        def complete_non_bt(path):
            ''' Complete a non-backtracking path to a full path
            '''

            while True:
                to_adds = set(range(len(graph))).difference(set(path))
                for to_add in to_adds:
                    connect_tos = set(path).intersection(set(graph[to_add]))
                    for connect_to in connect_tos:
                        insert_position = path.index(connect_to) + 1
                        path.insert(insert_position, connect_to)
                        path.insert(insert_position, to_add)
                if not to_adds:
                    break

            return path

        shortest_path = float("inf")
        for start in range(len(graph)):
            non_bts = non_back_tracking_path(start)

            for non_bt in non_bts:
                if len(non_bt) == len(graph):
                    return len(graph) - 1
                path = complete_non_bt(non_bt)
                shortest_path = min(shortest_path, len(path)-1)

        return shortest_path

def main():
    ''' Test shortestPathLength
    '''
    solution = Solution()

    test_cases = [
        [[1,2,3],[0],[0],[0]], # 4
        [[1],[0,2,4],[1,3,4],[2],[1,2]], # 4
        [[1,2,3,4],[0,2],[0,1],[0,5],[0,6],[3],[4]], #7
    ]
    for graph in test_cases:
        result = solution.shortestPathLength(graph)
        print(f"{graph}, {result}")

if __name__ == "__main__":
    main()
