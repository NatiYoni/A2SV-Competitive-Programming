# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(root):
           
            if not root:
                return (0,0)
      

            # result = (root.val + helper(root.left) + helper(root.right)) 
            left_sum, left_count = helper(root.left)
            right_sum, right_count = helper(root.right)

            total = left_sum + right_sum + root.val
            count = left_count + right_count + 1

            if total//count == root.val:
                self.ans += 1
            
            return (total, count)
        
        helper(root)
        return self.ans
            
            
            
