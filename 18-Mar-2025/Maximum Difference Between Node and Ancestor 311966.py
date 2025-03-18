# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def ancestor(root, min_, max_, diff):
               
            if not root:
                return diff
            
            max_ = max(max_, root.val)
            min_ = min(min_, root.val)            
            
            temp = max(abs(root.val - min_) ,abs(root.val - max_)) 
            diff = max(diff, temp)
            
            return max(ancestor(root.left, min_, max_, diff), ancestor(root.right, min_, max_, diff))

            

        return ancestor(root,float("inf"),float("-inf"), 0)