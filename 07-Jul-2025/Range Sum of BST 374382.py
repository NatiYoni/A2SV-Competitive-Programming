# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root,low,high):
            if not root:
                return 0
            
            ans = 0
            if root.val < low:
                return dfs(root.right,low,high)
            
            elif root.val > high:
                return dfs(root.left,low,high)
            
            else:
                ans += root.val  + dfs(root.left,low,high) + dfs(root.right,low,high)

            
            return ans
        
        return dfs(root,low,high)