# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        arr = []
        def largest(root,level):

            if not root:
                return 

            if level >= len(arr):
                arr.append(root.val)
            else:
                arr[level] = max(arr[level], root.val)

            largest(root.left,level + 1) 
            largest(root.right, level + 1)
            

        largest(root,0)
        
        return arr
            
