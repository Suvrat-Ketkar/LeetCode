#1123 Lowest Common Ancestor of Deepest Leaves
# Date: 04/04/2025
#Type: Daily Problem
# Method used: Depth First Search

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)  # (depth, LCA)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif left_depth < right_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)  # Current node is LCA

        return dfs(root)[1]
