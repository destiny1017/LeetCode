# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.recursive(root, low, high, 0)

           
    def recursive(self, node, low, high, sum):
        # print(node.val, node.right)
        if node.val >= low and node.val <= high:
            # print(f"add {node.val}")
            sum += node.val
        
        if node.left is not None:
            sum = self.recursive(node.left, low, high, sum)
        
        if node.right is not None:
            sum = self.recursive(node.right, low, high, sum)
        
        return sum