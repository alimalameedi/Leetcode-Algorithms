# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Solution 1
    # Time Complexity: O(n) - n being the number of nodes in the tree
    # Space Complexity: O(1)
    # Notes: Have a global max_diameter variable to keep track of the max diameter at any given node.
    #        Find maximum depth of each subtree, (max left depth + max right depth = diameter at a given node)
    #        Then compare that diameter to the global max_diameter and update the max if needed.

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            diameter = left_depth + right_depth
            self.res = max(self.res, diameter)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.res
