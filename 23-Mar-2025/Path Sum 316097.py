# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root,sum,flag):

            if not root:
                return False
            
            sum += root.val

            if not root.left and not root.right and sum == targetSum:
                return True

            return helper(root.left, sum,flag)  or  helper(root.right,sum,flag)
        
        return helper(root, 0,False)


        
            
