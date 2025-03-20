# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(left, right, depth):
            if not root:
                return 

            if not left and not right:
                return root

            if right and depth % 2 == 0:
                # print(depth, right.val,left.val)
                right.val, left.val = left.val, right.val
            

            reverse(left.left, right.right, depth + 1)
            reverse(left.right, right.left, depth + 1)


            
            return root
        
        return reverse(root.left, root.right,0)