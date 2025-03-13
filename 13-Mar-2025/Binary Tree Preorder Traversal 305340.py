# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def pre(root,arr):
            # if root:
            #     print(root.val) 

            # if root == None:
            #     return

            if root:
                arr.append(root.val)

                pre(root.left,arr)

                pre(root.right,arr)

            # else:
            #     return pre(root,arr)



            return arr
        
        arr = []
        return pre(root,arr) 
        
