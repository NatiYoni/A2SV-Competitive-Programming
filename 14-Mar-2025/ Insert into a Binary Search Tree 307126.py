# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            root = TreeNode(val)
            return  root

        else:
            if root.val > val:
                
                root.left = self.insertIntoBST(root.left, val)

                if root.left == None:
                    root.left = TreeNode(val)
                
                # print(root.val)
                return root 
            
            else:

                root.right = self.insertIntoBST(root.right, val)

                if root.right == None:
                    root.right = TreeNode(val)

                # print(root.val)
                return root

            