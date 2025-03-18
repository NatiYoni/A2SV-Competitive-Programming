# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root
        
        if root.val == q.val or root.val == p.val:
            return root
        
        return self.lowestCommonAncestor(root.left,p,q) if p.val < root.val else self.lowestCommonAncestor(root.right,p,q)
        
    

