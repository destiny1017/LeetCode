# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __dfs(self, node, value_list):
        if node is None:
            value_list.append(None)
        else:
            value_list.append(node.val)
            self.__dfs(node.left, value_list)
            self.__dfs(node.right, value_list)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first_list = []
        second_list = []
        self.__dfs(p, first_list)
        self.__dfs(q, second_list)
        print(first_list)
        print(second_list)
        return first_list == second_list
        