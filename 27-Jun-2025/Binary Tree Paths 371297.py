# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,path):
            if not root:
                return
                
            
            path.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(path.copy()))

            else :
                dfs(root.left,path)
                dfs(root.right,path)
            
            path.pop()
            return ans

        
        return dfs(root,[])
            

