# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Solution 1
        # Time Complexity: O(n) - n being the number of nodes in the tree
        # Space Complexity: O(1)
        # Notes: Use main function itself to perform recursion on
        #        inverting the tree, starting at the root

        if not root:
            return

        save = root.left
        root.left = root.right
        root.right = save

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # Solution 2
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Notes: This is only different in that we use a helper function
        #        to do the DFS instead of the main function.

        # def dfs(currNode):
        #     if not currNode:
        #         return
        #
        #     save = currNode.left
        #     currNode.left = currNode.right
        #     currNode.right = save
        #
        #     dfs(currNode.left)
        #     dfs(currNode.right)
        #
        # dfs(root)
        #
        # return root
