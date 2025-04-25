# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        arr = []

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            if root:
                arr.append(root.val)
            dfs(root.right)

        dfs(root)
        
        mid = len(arr) // 2



        
        def BST(arr):
            if not arr:
                return
            
            mid = len(arr)//2

            root = TreeNode(arr[mid])
            root.left = BST(arr[:mid])
            root.right = BST(arr[mid+1:])
        

            return root
        
        return BST(arr)

