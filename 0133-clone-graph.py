'''https://leetcode.com/problems/clone-graph/
'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self):
        self.originals = []
        self.copies = []

    def cloneGraph(self, node):

        if node == None:
            return None

        if not node.neighbors:
            return Node(node.val)

        if node in self.originals:
            return self.copies[self.originals.index(node)]

        new_node = Node(node.val)
        self.originals.append(node)
        self.copies.append(new_node)

        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))

        return new_node

# don't have testing code, will have to expand in the future, write a graph constructor based on the adjacency list.
