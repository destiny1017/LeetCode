# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inOrderTree(root, [])
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
    
    def inOrderTree(self, root, arr):
        if root.left is not None:
            self.inOrderTree(root.left, arr)
        
        arr.append(root.val)
        
        if root.right is not None:
            self.inOrderTree(root.right, arr)
        
        return arr