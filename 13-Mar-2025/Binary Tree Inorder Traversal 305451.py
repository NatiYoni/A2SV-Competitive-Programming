# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(root, arr):
            if root:
                inorder(root.left,arr)
                arr.append(root.val)
                inorder(root.right, arr)
                

            return arr
        arr = []
        return inorder(root, arr)
