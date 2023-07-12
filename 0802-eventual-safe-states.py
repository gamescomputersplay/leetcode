''' https://leetcode.com/problems/find-eventual-safe-states/
'''

class UniqueQueue:

    def __init__(self, values=[]):
        self.queue = values.copy()
        self.queue_set = set(self.queue)
        self.pointer = 0

    def add(self, values):
        for value in values:
            if value not in self.queue_set:
                self.queue.append(value)
                self.queue_set.add(value)

    def read(self):
        if self.pointer >= len(self.queue):
            return None
        self.pointer += 1
        return self.queue[self.pointer-1]
    
    def empty(self):
        if self.pointer == len(self.queue):
            return True
        return False

class Solution:
    def eventualSafeNodes(self, graph):

        # Terminal nodes are safe
        safe = set(i for i, node in enumerate(graph) if not node)
        unsafe = set()

        # Test other nodes
        for i, next_nodes in enumerate(graph):
            #print(i, next_nodes)
            # This node has been tested already
            if i in safe:
                continue

            # Stack to check paths from this node
            queue = UniqueQueue(next_nodes)

            # Nodes that have been looked at
            processed = {i}

            while True:

                node = queue.read()

                processed.add(node)
                #print("-", node, processed)

                # Path lead to an unsafe node
                if node in unsafe:
                    # This node is unsafe
                    unsafe.add(i)
                    break

                # Next nodes contain those we already processed - a cycle
                found_unsafe = False
                for next_node in graph[node]:
                    if next_node in processed and next_node not in safe:
                        unsafe.add(i)
                        found_unsafe = True
                        break
                    queue.add([next_node])
                if found_unsafe:
                    break

                # If queue is empty
                if queue.empty():

                    # Than all nodes we saw on the way are safe
                    safe.update(processed)
                    break

        return sorted(list(safe))

def main():
    ''' Test eventualSafeNodes
    '''
    solution = Solution()

    test_cases = [
        [[1,2],[2,3],[5],[0],[5],[],[]], #2456
        [[1,2,3,4],[1,2],[3,4],[0,4],[]], #4
        [[1],[]], #01
        [[]], #0
        [[0]], #-
        [[0],[1,2,3,4],[1,3,4],[2,4],[2]], #-
        [[],[0,2,3,4],[3],[4],[]], #01234
        [[1,2,3,4],[1,2,3,4],[3,4],[4],[]], #234
        [[1,2,3,4],[2],[1],[4],[]], #34
        [[1,3,4,5],[],[],[],[],[2,4]], #012345
        [[1,3,4,5],[],[],[],[2],[2,4]], #012345
    ]
    for graph in test_cases:
        result = solution.eventualSafeNodes(graph)
        print(f"{graph}, {result}")

if __name__ == "__main__":
    main()
