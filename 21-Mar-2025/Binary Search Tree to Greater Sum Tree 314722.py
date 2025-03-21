# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.n = 0
        def helper(root):
            if not root:
                return self.n
            
            # print(root.val)
            helper(root.right) 
            print(root.val)
            self.n += root.val
            root.val = self.n
            helper(root.left)
        
        helper(root)
        return root

        
