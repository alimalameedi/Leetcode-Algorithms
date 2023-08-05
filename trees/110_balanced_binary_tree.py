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
    # Notes: A null node will return [True, 0] - it is balanced (true) and has a max depth 0 on either side
    #        We want to find the max depth & balance status of each subtree left & right - is it balanced & max depth
    #        Something is balanced if its' left & right trees are balanced & if abs(maxDepthL - maxDepthR) <= 1
    #        then we can return [true/false, 1 + max(leftDepth, rightDepth). Any false will propagate up for failure.

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            left_tree = dfs(node.left)
            right_tree = dfs(node.right)

            balanced = left_tree[0] and right_tree[0] and abs(left_tree[1] - right_tree[1]) <= 1

            return [balanced, 1 + max(left_tree[1], right_tree[1])]

        return dfs(root)[0]
