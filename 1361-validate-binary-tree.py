''' https://leetcode.com/problems/validate-binary-tree-nodes/
'''

class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):

        # Find the root: node the no other node has as a child
        root_candidates = set(range(n)).difference(leftChild).difference(rightChild)

        # Valid tree has 1 root
        if len(root_candidates) != 1:
            return False
        root = list(root_candidates)[0]

        # Go through all the nodes from root
        # Children should not overlap
        stack = [root]
        seen = {root}

        while stack:

            node = stack.pop()

            # Same thing for left and right children
            for children in leftChild, rightChild:

                child = children[node]
                # Ignore empty cjhilred
                if child == -1:
                    continue

                # Any overlap means the tree is invalid
                if child in seen:
                    return False
                # Otherwise add it to the stack and list of seen nodes
                seen.add(child)
                stack.append(child)

        # If not all nodes were seen - invalid tree
        if len(seen) < n:
            return False

        return True

def main():
    ''' Test validateBinaryTreeNodes
    '''
    solution = Solution()

    test_cases = [
        (4, [1,-1,3,-1], [2,-1,-1,-1]), # True
        (4, [1,-1,3,-1], [2,3,-1,-1]), # False
        (2, [1,0], [-1,-1]), # False
        (1, [-1], [-1]), # True
        (2, [1, -1], [-1, -1]), # True
        (4, [1, 0, 3, -1], [-1, -1, -1, -1]), #False
    ]
    for n, leftChild, rightChild in test_cases:
        result = solution.validateBinaryTreeNodes(n, leftChild, rightChild)
        print(n, leftChild, rightChild, result)

if __name__ == "__main__":
    main()
