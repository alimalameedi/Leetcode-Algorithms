from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Time Complexity: O(n * m), where n is # of nodes in the subtree and m is # of nodes in the main tree
        # Space Complexity: O(1)

        # Base conditions for seeing if a tree is a subtree at its' lowest level:
        #           Empty subtree is a subtree of a tre.
        #           Empty tree is not able to have a subtree.

        def sameTree(p, q):

            if not p and not q:
                return True

            elif (not p and q) or (p and not q):
                return False

            elif p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        if not root:
            return False

        if not subRoot:
            return True

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
