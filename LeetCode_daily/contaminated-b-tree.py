#1261 Find Elements in a Contaminated Binary Tree
# Date: 21/02/2025
# Type: Daily Problem
# Method used: Trees,Recursion

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.recovered_values = set()  # Store recovered values for O(1) lookup
        self.recover_tree(self.root, 0)

    def recover_tree(self, node: TreeNode, value: int):
        if node is None:
            return
        
        node.val = value
        self.recovered_values.add(value)
        
        # Recursively recover the left and right children
        if node.left:
            self.recover_tree(node.left, 2 * value + 1)
        if node.right:
            self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.recovered_values

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)