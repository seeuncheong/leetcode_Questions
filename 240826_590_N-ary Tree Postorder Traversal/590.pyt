"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # if there's no root, return empty list
        if not root:
            return []

        result = []

        # define DFS function
        def dfs(root):
           # recursively call dfs for each child of the current node 
            for x in root.children:
                dfs(x)

            # append the value of the current node to the result list
            result.append(root.val)
        
        # start dfs from root
        dfs(root)

        # return the result list containing node values in post-order
        return result