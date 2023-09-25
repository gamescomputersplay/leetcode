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

        def try_adding_cycle(path, additional_nodes):
            ''' Tries to find a cycle that wouldvisit some nodes in additional nodes,
            and start and end in one of the nodes in path
            '''
            stack = [[start] for start in path]

            graph_copy = [[link for link in links if link in additional_nodes or node in additional_nodes]
                          for node, links in enumerate(graph)]

            while True:

                has_updates = False
                new_stack = []

                for so_far in stack:
                    if len(so_far) > 1 and so_far[0] == so_far[-1]:
                        new_stack.append(so_far)
                        continue
                    for potential_next in graph_copy[so_far[-1]]:
                        new_so_far = so_far.copy()
                        if potential_next not in so_far[1:]:
                            new_so_far.append(potential_next)
                            has_updates = True
                            new_stack.append(new_so_far)
                if not has_updates:
                    #print(stack)
                    return [cycle for cycle in stack if len(cycle) > 1 and cycle[0] == cycle[-1]]
                stack = new_stack

        def complete_non_bt(path):
            ''' Complete a non-backtracking path to a full path
            '''

            while True:
                to_adds = set(range(len(graph))).difference(set(path))
                #print(to_adds)
                additions = try_adding_cycle(path, to_adds)
                #print(additions)
                if not additions:
                    break

                addition = sorted(additions, key=lambda x: -len(x))[0]
                connect_at = path.index(addition[0])
                path = path[:connect_at] + addition + path[connect_at + 1:]
                if not to_adds:
                    break

            return path

        shortest_path = float("inf")
        for start in range(len(graph)):
            non_bts = non_back_tracking_path(start)
            # We might want to generate them all and pick longest

            for non_bt in non_bts:
                #print(non_bt)
                if len(non_bt) == len(graph):
                    return len(graph) - 1
                path = complete_non_bt(non_bt)
                #print("-", path)
                if len(set(path)) == len(graph):
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
        [[3],[3],[3,5],[0,1,2,6],[6],[2],[3,4]], #8
        [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]], 
    ]
    for graph in test_cases:
        result = solution.shortestPathLength(graph)
        print(f"{graph}, {result}")

if __name__ == "__main__":
    main()
