# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
       
        def dfs(root,val):
            if not root:
                return
            
            flag = True
            if root.val == val:
                flag = True
            else:
                flag =  False
                return

            if root.left:
                flag = dfs(root.left,val)
                if not flag:
                    return False

            if root.right:
                flag = dfs(root.right,val)
                if not flag:
                    return False

            return flag
        
        return dfs(root,root.val)